#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void){
    char *s = malloc(sizeof(char)*3);
    strcpy(s, "12");
    printf("s %p\n",s); // location of s[0]
    printf("s[0] %c\n",s[0]); // '1'
    printf("&s[0] %p\n", &s[0]); // lcoation of s[0]
    free(s);
}
