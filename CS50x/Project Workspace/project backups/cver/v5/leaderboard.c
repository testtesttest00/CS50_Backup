#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <cs50.h>

#include "leaderboard.h"

#define RECORDS "records.txt"

const int LENGTH = 16;
const int AUX = 8;

const unsigned int ARBITRARY = 7;
typedef node *table[ARBITRARY];
table hashtable = { NULL };


bool record(int moves){
    printf("\nEnter record to leaderboard?\n");
    int confirm = get_int("0-No 1-Yes\n");
    if (confirm != 1){
        return false;
    }
    printf("\n==-==-==-=-==-==-==-==-==-==-==-==-==-==-==-==\n");
    char *name;
    do{
        name = get_string("\nEnter name (maximum 16 characters)\n");
    } while(strlen(name) > LENGTH || strlen(name) < 1);
    char *parsed = parse(name);
    if (parsed == NULL){
        return false;
    }
    FILE *ranklist = fopen(RECORDS, "a");
    if (ranklist == NULL){
        return false;
    }
    fprintf(ranklist, "%s,%i\n", parsed, moves);
    fclose(ranklist);
    if (name != parsed){
        free(parsed);
    }
    return true;
}


char *parse(char *pre){
    bool comma_flag = false;
    int len = strlen(pre);
    for (int i = 0; i < len; i++){
        if (pre[i] == ','){
            comma_flag = true;
        }
    }

    if (comma_flag){
        int bytes = len + 3; // not exactly bytes, just know that +3 for to give space for " " \0 characters
        char *post = malloc(bytes*sizeof(char));
        if (post == NULL){
            return NULL;
        }
        post[0] = '"';
        for (int i = 0; i < len; i++){
            post[i+1] = pre[i];
        }
        post[len+1] = '"';
        post[len+2] = '\0';
        return post;
    }
    return pre;
}


bool printrank(void){
    FILE *ranklist = fopen(RECORDS, "r");
    char line[LENGTH+AUX];
    printf("\nRecorded Scores\n\nMoves  Name\n");
    while (fgets(&line[0], LENGTH+AUX, ranklist)){
        char backupline[LENGTH+AUX];
        strcpy(backupline, line);
        char *name = readcsv(line, 1);
        int moves = atoi(readcsv(backupline, 2));
        loadhash(moves,name);
        printf("%5i  %s  in %i\n", moves, name, hash(moves));
    }

    //test: mergesort
    node *n = mergesort(hashtable[6]);
    while(n != NULL){
        printf("%p <@ %5i / %s p> %p\n", n, n->moves, n->name, n->next);
        n = n->next;
    }

    printf("\n==-==-==-=-==-==-==-==-==-==-==-==-==-==-==-==\n");
    for(int i = 0; i < ARBITRARY; i++){
        freehash(hashtable[i]);
    }
    fclose(ranklist);
    return true;
}


char *readcsv(char *line, int iter){
    int len = strlen(line);
    int mem[LENGTH] = { 0 };
    bool in_quotation = false;
    if(line[0] == '"'){
        in_quotation = true;
        for (int i = 1; i < len+1; i++){
            if (line[i] == '"'){
                in_quotation = !in_quotation;
            }
            if (in_quotation && line[i] == ','){
                mem[i-1] = 1;
                line[i] = ' ';
            }
        }
    }

    char *token;
    for(token = strtok(line, ","); token && *token; token = strtok(NULL, "\n")){
        if (!--iter){
            if (token[0] == '"'){
                token = &token[1];
                token[strlen(token)-1] = '\0';
                for (int i = 0; i < LENGTH; i++){
                    if (mem[i] == 1){
                        token[i] = ',';
                    }
                }
                return token;
            }
            return token;
        }
    }
    return NULL;
}


// 2) merge sort function taking in hash table pointer to sort respective linked list
// 3) fill up a list of 10 nodes, sorting next hash table list when needed
// 4) print move/name of 10 nodes


int hash(int moves){
    if (moves > 0 && moves <= 40){
        return 0;
    }
    else if (moves > 40 && moves <=80){
        return 1;
    }
    else if (moves > 80 && moves <=110){
        return 2;
    }
    else if (moves > 110 && moves <=130){
        return 3;
    }
    else if (moves > 130 && moves <=150){
        return 4;
    }
    else if (moves > 150 && moves <=180){
        return 5;
    }
    else if (moves >180){
        return 6;
    }
    return -1;
}


node *loadhash(int moves, char *name){
    int index = hash(moves);
    // node *start = (hashtable[index] == NULL) ? (hashtable[index] = malloc(sizeof(node))) : hashtable[index];
    node *n = malloc(sizeof(node));
    n->moves = moves;
    strcpy(n->name, name);
    n->next = hashtable[index];
    hashtable[index] = n;

    return n;
}


bool freehash(node *next){
    while(next!=NULL){
        node *temp = next->next;
        free(next);
        next = temp;
    }
    return true;
}


// currently able to split & merge linked list of length 2 (left to add recursive function)
node *mergesort(node *linkedlist){ //, int nodecount){
    if (linkedlist == NULL){
        return NULL;
    }
    /* if (nodecount == 0){
        node *n = linkedlist;
        while(n != NULL){
            n = n->next;
            nodecount++;
        }
    } */
    int nodecount = 0;
    node *loop = linkedlist;
    while (loop != NULL){
        nodecount++;
        loop = loop->next;
    }

    int counter = nodecount / 2; // even count eg4,l=2(4/2=2),r=2(to null) ,, odd count eg5,l=2((int)5/2 = 2),r=3(to null)
    node *left = linkedlist;
    node *loopl = left;
    node *right = NULL;
    while (counter > 0){
        if (!--counter){
            right = loopl->next;
            loopl->next = NULL;
        }
        loopl = loopl->next;
    }
    node* merged = mergesort_merge(left, right);
    //expect: split lists end with NULL;
    //after merging all nodes, hashtable[index] = node *merge (to point to new 1st element of linked list)
    return merged;
}


node *mergesort_merge(node *list1, node* list2){
    if (!list1){
        return list2;
    }
    else if (!list2){
        return list1;
    }
    else if (!(list1 && list2)){
        return NULL;
    }

    node *head;
    node *tail;
    if (list1->moves <= list2->moves){
        head = list1;
        tail = list1;
        list1 = list1->next;
        tail->next = NULL;
    }
    else{
        head = list2;
        tail = list2;
        list2 = list2->next;
        tail->next = NULL;
    }

    while (list1 || list2){
        if (!list1){
            tail->next = list2;
            break;
        }
        else if (!list2){
            tail->next = list1;
            break;
        }

        if (list1->moves <= list2->moves){
            tail->next = list1;
            list1 = list1->next;
            tail = tail->next;
            tail->next = NULL;
        }
        else{
            tail->next = list2;
            list2 = list2->next;
            tail = tail->next;
            tail->next = NULL;
        }
    }

    return head;
}
