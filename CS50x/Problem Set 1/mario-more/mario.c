#include <cs50.h>
#include <stdio.h>

void blanks(int height, int row);
void blocks(int height, int row);

int main(void){
    int height;
    do{
        height = get_int("Height: ");
    }while(height < 1);

    for(int x = 0; x < height; x++){
        blanks(height, x);
        blocks(height, x);
        printf("  ");
        blocks(height, x);
        printf("\n");
    }
}

void blanks(int height, int row){
    for(int blanks = 1; blanks < height - row; blanks++){
        printf(" ");
    }
}

void blocks(int height, int row){
    for(int blocks = height - row; blocks < height + 1; blocks++){
        printf("#");
    }
}
