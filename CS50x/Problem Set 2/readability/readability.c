#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>
#include <math.h>

float calc(string text);

int main(void){
    string text = get_string("Text: ");
    int cl_index = round(calc(text));
    if (cl_index < 1){
        printf("Before Grade 1\n");
    }
    else if (cl_index > 16){
        printf("Grade 16+\n");
    }
    else{
        printf("Grade %i\n", cl_index);
    }
}

float calc(string text){
    int len = strlen(text);
    int letters = 0;
    int sentences = 0;
    int words = 1;
    for(int i = 0; i < len; i++){
        if(isalpha(text[i])){
            letters += 1;
        }
        else if(isspace(text[i])){
            words += 1;
        }
        else if((int)text[i] == 33 || (int)text[i] == 46 || (int)text[i] == 63){
            sentences += 1;
        }
    }
    float l = (float) letters / words * 100;
    float s = (float) sentences / words * 100;
    return 0.0588 * l - 0.296 * s - 15.8;
}
