// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>

#include "dictionary.h"

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

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

int word_count = 0;

void table_init(void){
    for (int i = 0; i < N; i++){
        //table[i] = malloc(sizeof(node*));
        table[i] = NULL;
        //printf("Successfully initialized table[%d]\n", i);
    }
}

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    char *w = malloc(LENGTH + 1);
    for (int i = 0; i < LENGTH + 1; i++){
        if(word[i] == '\0'){
            w[i] = '\0';
            break;
        }
        w[i] = tolower(word[i]);
    }
    unsigned int index = hash(w);
    if(table[index]==NULL){
        free(w);
        return false;
    }
    for(node *n = table[index]; n != NULL; n = n->next){
        //printf("check %s ->>>->>>->>> %p\n",n->word, n->next);
        if (strcmp(w, n->word) == 0){
            //printf("%s :::::::: %s\n", word, n->word);
            free(w);
            return true;
        }
    }
    free(w);
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
    FILE *dict = fopen(dictionary, "r");
    char buffer[1];
    char *word = malloc(sizeof(char) * (LENGTH + 1));
    if (word == NULL){
        return false;
    }
    int len = 0;

    while(fread(buffer, sizeof(char), 1, dict)){
        //printf("%c\n", *buffer);
        if(isalpha(*buffer) || *buffer == '\''){
            word[len] = *buffer;
            len++;
        }
        else{
            word[len] = '\0';
            //word = realloc(word, len+1);
            len = 0;
            //if (word == NULL){
            //    word_count = 0;
            //    return false;
            //}
            //printf("%s\n", word);
            word_count++;

            node *n = malloc(sizeof(node));
            if (n == NULL){
                word_count = 0;
                return false;
            }
            //printf("%s\n", word = strcpy(n->word, word));
            //printf("%s\n", n->word);
            //printf("%s\n", word);
            strcpy(n->word, word);//n -> word = *word;
            //printf("%s\n", n->word);
            unsigned int index = hash(word);
            //printf("%i\n", index);
            n -> next = table[index];
            table[index] = n;

            //word = realloc(word, LENGTH+1);
            //if (word == NULL){
            //    word_count = 0;
            //    return false;
            //}
        }
    }

    free(word);
    fclose(dict);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    return word_count;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    bool error = false;
    for (int i = 0; i < N; i++){
        if (table[i] != NULL){
// Method 1: For loop
            //node *temp = malloc(sizeof(node));
            node *temp;
            for (node *n = table[i]; n != NULL; n = temp){//n = temp -> next){
                if (n == NULL){                                    // im guessing memory is stored here hence why this is possible V
                    error = true;                                  // for (node *n = table[i]; n != NULL; n = n->next){
                    break;                                         //    if (n == NULL){
                }                                                  //        error = true;
                temp = n->next; //temp -> next = n -> next;        //        break;
                //printf("free'd %s @ %p\n", n->word, n);          //    }
                free(n);                                           // free(n);
            }                                                      // }      n = n->next even though n->next should have been free'd
            //free(temp);                                          // hence why valgrind flags this with error, 8 bytes unreachable?

// Method 2: While loop
//            node *n = table[i];
//            while(n != NULL){
//                //node *temp = malloc(sizeof(node*));
//                //temp = n -> next;
//                // ^^ this would replace whole temp ptr, losing reference to malloced memory
//                // making any free(temp) after this to be equivalent to free(n->next);
//                node *temp;
//                temp = n -> next;
//                //printf("free'd %s @ %p\n", n->word, n);
//                free(n);
//                n = temp;
//            }
        }
        if (error){
            break;
        }
    }
    return !error;
}
