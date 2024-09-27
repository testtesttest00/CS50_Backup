#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Max number of candidates
#define MAX 9

// preferences[i][j] is number of voters who prefer i over j
int preferences[MAX][MAX];

// locked[i][j] means i is locked in over j
bool locked[MAX][MAX];

// Each pair has a winner, loser
typedef struct
{
    int winner;
    int loser;
} pair;

// Array of candidates
string candidates[MAX];
pair pairs[MAX * (MAX - 1) / 2];

int pair_count;
int candidate_count;

// Function prototypes
bool vote(int rank, string name, int ranks[]);
void record_preferences(int ranks[]);
void add_pairs(void);
void sort_pairs(void);
void lock_pairs(void);
void print_winner(void);

int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: ./tideman [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX)
    {
        printf("Maximum number of candidates is %i\n", MAX);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i] = argv[i + 1];
    }

    // Clear graph of locked in pairs
    for (int i = 0; i < candidate_count; i++)
    {
        for (int j = 0; j < candidate_count; j++)
        {
            locked[i][j] = false;

            preferences[i][j] = 0;
        }
    }

    pair_count = 0;
    int voter_count = get_int("Number of voters: ");

    // Query for votes
    for (int i = 0; i < voter_count; i++)
    {
        // ranks[i] is voter's ith preference
        int ranks[candidate_count];

        for(int j = 0; j < candidate_count;j++){
            ranks[j] = -1;
        }

        // Query for each rank
        for (int j = 0; j < candidate_count; j++)
        {
            string name = get_string("Rank %i: ", j + 1);

            if (!vote(j, name, ranks))
            {
                printf("Invalid vote.\n");
                return 3;
            }
        }

        record_preferences(ranks);

        printf("\n");
    }

    add_pairs();
    sort_pairs();
    lock_pairs();
    print_winner();
    return 0;
}

// Update ranks given a new vote
bool vote(int rank, string name, int ranks[])
{
    for (int i = 0; i < candidate_count; i++){
        if (strcmp(name, candidates[i]) == 0){
            for (int j = 0; j < candidate_count; j++){
                if (ranks[j] == i){
                    return false;
                }
            }
            ranks[rank] = i;
            return true;
        }
    }
    return false;
}

// Update preferences given one voter's ranks
void record_preferences(int ranks[])
{
    //for (int i = 0, compare = (candidate_count/2)(candidate_count-1); i < compare; i++){}
    for (int i = 0; i < candidate_count; i++){
        for (int j = i + 1; j < candidate_count; j++){
            preferences[ranks[i]][ranks[j]]++;
            //preferences[ranks[j]][ranks[i]]--;
            //printf("%s %i %s\n", candidates[i], preferences[ranks[i]][ranks[j]], candidates[j]);
        }
    }
//    for (int i = 0; i < candidate_count; i++){
//        for (int j = 0; j < candidate_count; j++){
//            printf("%s has %i votes more than %s\n",candidates[i] ,preferences[i][j] , candidates[j]);
//        }
//        printf("\n");
//    }
    return;
}

// Record pairs of candidates where one is preferred over the other
void add_pairs(void)
{
    for (int i = 0; i < candidate_count; i++){
        for (int j = 0; j < candidate_count; j++){
            int balance = preferences[i][j] - preferences[j][i];
            if (balance > 0){
                pair_count++;
                pairs[pair_count - 1].winner = i;
                pairs[pair_count - 1].loser = j;
            }
        }
    }
    //printf("%i pairs\n", pair_count);
    //for (int i = 0; i < pair_count; i++){
    //    printf("%i  winner: %s loser: %s | diff: %i\n", i, candidates[pairs[i].winner], candidates[pairs[i].loser], preferences[pairs[i].winner][pairs[i].loser]);
    //}
    return;
}

// Sort pairs in decreasing order by strength of victory
void sort_pairs(void)
{
    for (int j = 0; j < pair_count - 1; j++){
        int highest = j;
        for (int i = j + 1; i < pair_count; i++){
            if (preferences[pairs[i].winner][pairs[i].loser] > preferences[pairs[highest].winner][pairs[highest].loser]){
                highest = i;
            }
        }
        pair temp = pairs[j];
        pairs[j] = pairs[highest];
        pairs[highest] = temp;
    }
    //for (int i = 0; i < pair_count; i++){
    //    printf("sorted| %i  winner: %s loser: %s | diff: %i\n", i, candidates[pairs[i].winner], candidates[pairs[i].loser], preferences[pairs[i].winner][pairs[i].loser]);
    //}
    return;
}

// Lock pairs into the candidate graph in order, without creating cycles
void lock_pairs(void)
{
    bool cycle = 0;
    int lock_count = 0;
    for (int i = 0; i < pair_count; i++){
        int lost = pairs[i].loser;
        int temp = lost;
        //int temp = lost;
        for (int j = 0; j < lock_count; j++){
            for (int k = 0; k < candidate_count; k++){
                if (locked[lost][k] == true){
                    //printf("j: %i  ", j);
                    temp = k;
                    //temp = k;
                    if (k == pairs[i].winner){
                        cycle = 1;
                        //printf("cycle detected\n");
                    }
                }
            }
            lost = temp;
            //lost = temp;
        }
        if (!cycle){
            locked[pairs[i].winner][pairs[i].loser] = true;
            //printf("locked %s --> %s (%i)\n", candidates[pairs[i].winner], candidates[pairs[i].loser], preferences[pairs[i].winner][pairs[i].loser]);
            lock_count++;
        }
        cycle = 0;
    }
    return;
}

// Print the winner of the election
void print_winner(void)
{
    for (int i = 0; i < candidate_count; i++){
        //printf("i%i\n", i);
        for (int j = 0; j < candidate_count; j++){
            if (locked[j][i] == true){
                //printf("%s locked over %s\n",candidates[j],candidates[i]);
                break;
            }
           // printf("j%i\n", j);
            if (j == candidate_count - 1){
                printf("%s\n", candidates[i]);
            }
        }
    }
    return;
}
