#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>

bool key_error(string text);

int main(int argc, string argv[]){
    if (argc == 2){
        if (key_error(argv[1]) == false){
            string key = argv[1];
            string text = get_string("plaintext:  ");
            for (int i = 0, len = strlen(text); i < len; i++){
                if (isalpha(text[i])){
                    int index = (int) toupper(text[i]) - 65;
                    char newalpha = toupper(key[index]);
                    if (islower(text[i])){
                        newalpha = tolower(newalpha);
                    }
                    text[i] = newalpha;
                }
            }
            printf("ciphertext: %s\n", text);
        }
        else{
            printf("Invalid key.\n");
            return 1;
        }
    }
    else{
        printf("Usage: ./substitution key\n");
        return 1;
    }
}

bool key_error(string text){
    int len = strlen(text);
    if (len != 26){
        return 1;
    }
    else{
        int duplicate[26] = {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0};
        for (int i = 0; i < len; i++){
            if (isalpha(text[i]) == false){
                return 1;
            }
            else{
                if (duplicate[toupper(text[i])-65] == true){
                    return 1;
                }
                else{
                    duplicate[toupper(text[i])-65] = true;
                }
            }
        }
    }
    return 0;
}
