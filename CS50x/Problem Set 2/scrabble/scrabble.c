#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>

int points(string word);

int main(void){
    string word1 = get_string("Player 1: ");
    string word2 = get_string("Player 2: ");
    int pt1 = points(word1);
    int pt2 = points(word2);
    if (pt1 > pt2){
        printf("Player 1 wins!\n");
    }
    else if (pt1 < pt2){
        printf("Player 2 wins!\n");
    }
    else{
        printf("Tie!\n");
    }
}

int points(string word){
    int value[] = {1,3,3,2,1,4,2,4,1,8,5,1,3,1,1,3,10,1,1,1,1,4,4,8,4,10};
    int total = 0;
    for(int i = 0, l = strlen(word); i < strlen(word); i++){
        if(isalpha(word[i])){
            int c = toupper(word[i]);
            total += value[c - 65];
        }
    }
    return total;
}
