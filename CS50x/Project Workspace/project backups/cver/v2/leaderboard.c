#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <cs50.h>

#include "leaderboard.h"

#define RECORDS "records.txt"

const int LENGTH = 16;
const int AUX = 8;

typedef struct node{
    char *name;
    int moves;
    struct node *next;
} node;

typedef node *table[5];

table *tableptr_arr[2] = { NULL };


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
        int bytes = len + 3;
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
        printf("%5i  %s\n", moves, name);
    }
    //printf ( loop for each line from hash table up to top 10 ) *sprintf to format if needed (:3.0f for moves)
    printf("\n==-==-==-=-==-==-==-==-==-==-==-==-==-==-==-==\n");
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
    for(token = strtok(line, ","); token && *token; token = strtok(NULL, "\n")){ // if token == NULL return false && if *token == '\0'return false
        if (!--iter){ // let iter = 1(1st tok) !--iter = !(iter--) = !(1--) = !0 = true VS !iter-- = if(!1)-- = if(false)-- >> iter -- after check
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

/*
bool loadhash(int moves, char *name){
    table *activetable;
    if (moves <= 100){
        activetable = (tableptr_arr[0] == NULL) ? (tableptr_arr[0] = malloc(sizeof(table))) : tableptr_arr[0];
    }
    else if (moves > 100){
        activetable = (tableptr_arr[1] == NULL) ? (tableptr_arr[1] = malloc(sizeof(table))) : tableptr_arr[1];
    }
    if (activetable == NULL){
        return false;
    }

    if (moves / 100 > 2 || move % 100 > 80){
        node *emptynode;
        if (activetable[5] == NULL){
            activetable[5] = malloc(sizeof(node));
            emptynode = activetable[5];
        }

    }
    return true;
}
bool loadhash(int moves, char *name){
    return true;
}
bool printhash(int limit_top){
    return true;
}
bool unloadhash(void){
    return true;
}
*/
