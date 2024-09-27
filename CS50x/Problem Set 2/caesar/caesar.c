#include <stdio.h>
#include <stdlib.h>
#include <cs50.h>
#include <ctype.h>
#include <string.h>

bool checknum(string inp);

int main(int argc, string argv[]){
    if(argc == 2 && checknum(argv[1])){
        int key = atoi(argv[1]);
        string text = get_string("plaintext:  ");
        for(int i = 0, len = strlen(text); i < len; i++){
            if (isalpha(text[i])){
                int newalpha = (toupper(text[i]) - 65 + key) % 26 + 65;
                if (islower(text[i])){
                    newalpha = tolower(newalpha);
                }
                text[i] = newalpha;
            }
        }
        printf("ciphertext: %s\n", text);
    }
    else{
        printf("Usage: ./caesar key\n");
        return 1;
    }
}

bool checknum(string inp){
    int valid = 1;
    for(int i = 0, len = strlen(inp); i < len; i++){
        valid = valid * isdigit(inp[i]);
    }
    return (bool) valid;
}
