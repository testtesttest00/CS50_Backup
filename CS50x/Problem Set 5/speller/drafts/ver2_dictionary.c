// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>

#include "dictionary.h"

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

const unsigned int N = 26;

// Hash table
node *table[N];
void table_init(void){
    for(int i = 0; i < N; i++){
        table[i] = malloc(sizeof(node*));
    }
    for(int i = 0; i < N; i++){
        table[i] -> next = NULL;
    }
}
int loaded_words = 0;

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    if(table[hash(word)] == NULL){
        return false;
    }
    for(node *n = table[hash(word)]; n != NULL; n = n->next){
        if (strcmp(word, n->word) == 0){
            return true;
        }
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    return toupper(word[0]) - 'A';
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    table_init();
    bool error = false;
    FILE *dict = fopen(dictionary, "r");
    if (dict == NULL){
        printf("Unable to open \"%s\"\n", dictionary);
        return !error;
    }
    char buffer;
    char *word = malloc(sizeof(char)*(LENGTH + 1));
    if (word == NULL){
        error = true;
        return error;
    }
    bool end_flag = false;
    int len = 0;

    while(fread(&buffer, sizeof(char), 1, dict)){ //can use fgetc?
        if (isalpha(buffer) || buffer == '\''){
            word[len] = buffer;
            len++;

            if (buffer == 'n' && end_flag){ // buffer == "n" > compares char buffer vs string n: wrong
                // Save existing word to memory, in a hash table
                word = realloc(word, len + 1); //cant realloc a static allocation (done when using char word[47])
                if (word == NULL){
                    error = true;
                    break;
                }
                node *n = malloc(sizeof(node));
                strcpy(n->word, word);// n -> word = *word; wont work as cant directly assign char arrays
                n -> next = table[hash(word)] -> next;
                table[hash(word)] -> next = n;
                loaded_words++;
            }
        }
        else if (buffer == '\\'){
            word[len] = '\0'; //'\0' references single NUL char vs "\0" representing a string
            end_flag = true;
        }
    }

    free(word);
    if(error){
        loaded_words = 0;
    }

    return !error;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    return loaded_words;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    bool error = false;
    node *temp = malloc(sizeof(node));
    for (int i = 0; i < N; i++){
        if (table[i] != NULL){
            for (node *n = table[i]->next; n != NULL; n = n -> next){
                temp -> next = n -> next;
                if (n == NULL){
                    error = true;
                    break;
                }
                free(n);
            }
        }
        if (error){
            break;
        }
    }
    free(temp);
    for(int i = 0; i < N; i++){
        free(table[i]);
    }
    return !error;
}
