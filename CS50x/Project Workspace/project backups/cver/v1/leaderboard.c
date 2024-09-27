#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <cs50.h>

#include "leaderboard.h"

const int LENGTH = 16;

bool record(int moves){
    printf("\nEnter record to leaderboard?\n");
    int confirm = get_int("0-No 1-Yes\n");
    if (confirm != 1){
        return false;
    }

    printf("\n==-==-==-=-==-==-==-==-==-==-==-==-==-==-==-==\n");
    char *name = get_string("\nEnter name:\n");
    do{
        printf("\nName too long (maximum 16 characters)\n");
        name = get_string("Enter name:\n");
    } while(strlen(name) > LENGTH || strlen(name) < 1);
    char *parsed = parse(name);
    if (parsed == NULL){
        return false;
    }
    FILE *ranklist = fopen("records.txt", "a");
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
