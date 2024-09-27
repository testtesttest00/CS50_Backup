// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>

#include "dictionary.h"

//#include <string.h>
#include <stdio.h>

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 26;

// Hash table
node *table[N];
node **table_arr[LENGTH]; // "*" can be stacked as many times as needed to represent multiple levels of pointers
for (int i = 0; i < LENGTH; i++){
                table = malloc(sizeof(node*) * N);
                if (table == NULL){
                    printf("Insufficient memory at hash table %i", i);
                    break;
                }
                for (int j - 0; j < N; j++){
                    table[j] -> next = NULL;
                }
                table_arr[i] = table;
            }

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    //word_len = strlen(word);
    first_char = toupper(word[0]) - 'A';
    return first_char; //+ word_len*100
    // returns AABB, AA is wordlen, BB is firstchar (A[0] and B[0] could be 0, eg A-A-0-B, A-B-B or A-0-B)
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    FILE *dict = fopen(dictionary, "r");
    char buffer;
    char word[LENGTH + 1];
    int word_len = 0;
    bool end_flag = false;

    while (fread(dict, sizeof(char), 1, &buffer)){
        if (isalpha(buffer) && !end_flag){
            word[word_len] = buffer;
            word_len++;
        }
        else if (buffer == "\\"){
            end_flag = true;
        }
        else if (buffer == "n" && word_len > 0 && end_flag){
            word[word_len] = "\0";
//node**table_arr[LENGTH];>>>to access and get length 1 table, node *tlen1 = table_arr[0];
//node *table[26];        >>>to access and place "a", tlen1[0] -> word = "a" or simply table_arr[0][0] -> "a"
            //node *temp_table = table_arr[word_len];
            //temp_table[hash(word)] -> word = word;
            node *start = table_arr[word_len][hash(word)];
            node *n = malloc(sizeof(node));
            n -> word = word;
            n -> next = start -> next;
            start -> word = word;
            start -> next =
            word_len = 0;
            end_flag = false;
        }
    }
    return false;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return 0;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    return false;
}
