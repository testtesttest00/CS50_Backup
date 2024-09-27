#include <cs50.h>
#include <stdio.h>

int main(void){
    int height;
    do{
        height = get_int("Height: ");
    }while(height < 1);

    for(int x = 0; x < height; x++){
        for(int blanks = 1; blanks < height - x; blanks++){
            printf(" ");
        }
        for(int blocks = height - x; blocks < height + 1; blocks++){
            printf("#");
        }
        printf("\n");
    }
}
