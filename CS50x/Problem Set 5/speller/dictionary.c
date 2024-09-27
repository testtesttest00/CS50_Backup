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

// Number of buckets in hash table
const unsigned int N = 26;

// Hash table
typedef node *table[N];
table *tableptr_arr[LENGTH];

// Do tableptr_arr[strlen] = malloc(sizeof(table)); then table_init(tableptr_arr[strlen]); if tableptr_arr[strlen] == NULL;
void table_init(table *table_ptr){
    for(int i = 0; i < N; i++){
        (*table_ptr)[i] = NULL;
    }
}

void table_arr_init(void){
    for (int i = 0; i < LENGTH; i++){
        tableptr_arr[i] = NULL;
    }
}

int word_count = 0;

void print_table(table *ptr[LENGTH]){
    //prints each word in each table in tabarr, indicating len, hash

//theory:
//
//node *i  = n[j] << node *n[_] << node **x = &n (a pointer to 1st element(a node*) of array) ie a node ptr array ptr is (node **) << node **x = table *x = tableptr_arr[i] << table *tableptr_arr[_]
//^(node *) *ptr[i][j]    ^(node *[_]) *ptr[i]    ^(node **) aka (table *) ptr[i]                                                     ^(table *) ptr[i]                        ^(table *[_]) ptr
//
//or
//
//node *i = *n << node **n  = &((node **x)[j]) << node **x = &n (a pointer to 1st element(a node*) of array) ie a node ptr array ptr is (node **) << node **x = table *x = tableptr_arr[i] << table *tableptr_arr[_]
//^(node *) *ptr[i][j]     ^(node **) ptr[i][j]     ^(node **) aka (table *) ptr[i]                                                                  ^(table *) ptr[i]                        ^(table *[_]) ptr

    //printf("\n(ptr)%p\n", ptr); //ptr = location of len1 table's pointer (malloced space to place every table's ptrs)
    //printf("(ptr[0])%p\n", ptr[0]); //ptr[0] = location of len1 table
    //printf("(ptr[0][0])%p\n\n", ptr[0][0]); //ptr[0][0] = location of 'a' node pointer

    for (int i = 0; i < LENGTH; i++){
        printf("len %.2i @ %p <- %p\n", i+1, ptr[i], &ptr[i]);
//ptr[i] = pointer to leni table
//&ptr[i] = location of leni table's pointer on tabarray (from the malloced space to place every table's ptrs)
        if(ptr[i]!=NULL){
            for (int j = 0; j < N; j++){
                printf("    %c -> %p @ %p\n", j+'a', (*ptr[i])[j], (&(*ptr[i])[j])); //@ %p -> %p\n", j+'a', ptr[i][j], *ptr[i][j]);
//table is node pointer array
//ptr[i][j] = jth element of the array of leni table pointer. table pointer = pointer to a node pointer
//*ptr[i][j] = jth node pointer
                for(node *n = (*ptr[i])[j]; n != NULL; n = n->next){
                    printf("         %p -> \"%s\" -> %p\n", n, n->word, n->next);//\"%s\" @ %p -> %p\n", n->word, n, n->next);
                }
            }
        }
    }
}

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    int len = strlen(word);
    int index = hash(word);
    char *w = malloc(LENGTH + 1);
    for (int i = 0; i < LENGTH + 1; i++){
        if(word[i] == '\0'){
            w[i] = '\0';
            break;
        }
        w[i] = tolower(word[i]);
    }
    table *tableptr = tableptr_arr[len-1];
    if (tableptr == NULL){
        //printf("&tableptr %p ", &tableptr_arr[len-1]);
        //printf(" %i ", 0);
        free(w);
        return false;
    }
    node *nodeptr = (*tableptr)[index];
    if (nodeptr == NULL){
        //printf("&nodeptr %p nodeptr %p", &*tableptr[index], *&*tableptr[index]);
        //printf(" %i ", 1);
        free(w);
        return false;
    }
    for(; nodeptr != NULL; nodeptr = nodeptr -> next){
        //printf("%s : found %s\n", w, nodeptr->word);
        if (strcmp(w, nodeptr->word) == 0){
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
    FILE *dict = fopen(dictionary, "r");
    char buffer = ' ';
    char *word = malloc(sizeof(char)*(LENGTH+1));
    if (word == NULL){
        return false;
    }
    int len = 0;
    table_arr_init();
    //print_table(tableptr_arr);

    while(fread(&buffer, sizeof(char), 1, dict)){
        if (isalpha(buffer) || buffer == '\''){
            word[len] = tolower(buffer);
            len++;
        }
        else{
            word[len] = '\0';

            //enter word into hash table
            int index = hash(word);
            table *tableptr = tableptr_arr[len-1];
            if (tableptr == NULL){
                tableptr = malloc(sizeof(table));
                if (tableptr == NULL){
                    return false;
                }
                tableptr_arr[len-1] = tableptr;
                table_init(tableptr);
            }
            node *n = malloc(sizeof(node)); // can't use node n; or free(n) > n will remain @ same ptr causing recursive linked list
            if (n == NULL){
                    return false;
                }
            //printf("%p ", n);
            strcpy(n->word, word);
            //printf("%s stored tableptr_arr[%i] table[%i]\n", n->word, len-1, index);
            //printf("%p ", tableptr);
            //printf("%p ", (*tableptr)[index]);
            //printf("%s len:%i tableptr:%p tableptr item:%p, index: %i\n", word, len, tableptr, *tableptr[index], index);
            n->next = (*tableptr)[index];
            (*tableptr)[index] = n;
            //printf("node: word - %s, next - %p | @ %p | \n", n->word, n->next, n);
            //printf("%p\n", (*tableptr)[index]);

            len = 0;
            word_count++;
        }
    }

    free(word);
    //print_table(tableptr_arr);
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
    for(int i = 0; i < LENGTH; i++){
        table *tableptr = tableptr_arr[i];
        if (tableptr != NULL){
            for(int j = 0; j < N; j++){
                //printf("%p is equivalent to %p", (*tableptr)[j], *(tableptr[j]));
                //printf("\nword is %s, location %p\n", ((*tableptr)[j])->word, &((*tableptr)[j]));
                //return false;
                //printf("\n%p\n", tableptr);
                node *nodeptr = (*tableptr)[j];
                while(nodeptr != NULL){
                    node *temp = nodeptr -> next;
                    free(nodeptr);
                    nodeptr = temp;
                }
            }
        }
        free(tableptr);
    }
    return true;
}
