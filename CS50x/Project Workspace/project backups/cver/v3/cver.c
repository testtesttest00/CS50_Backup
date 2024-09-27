#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <time.h>
#include <cs50.h>

#include "leaderboard.h"

const int ROW = 4;
const int COL = 4;
const int SCRAMBLE = 500;

typedef struct board {
    char *value[ROW][COL];
    int turns;
} board;


board *init(void);
board *move(board *game, int direction);
bool checkwin(board *game);
int printboard(board *game);
void next(board *game);


int main(void){
    board *game = init();
    game = move(game,0);

    while (!checkwin(game)){
        next(game);
    }
    if (checkwin(game)){
        printf("\n==-==-==-=-==-==-==-==-==-==-==-==-==-==-==-==\n");
        printf("\nYou won\n");
        printboard(game);
        printf("Total: %i moves\n\n", game->turns);
    }

    if (record(game->turns)){
        printf("\nYour score was successfully recorded\n");
    }
    else{
        printf("\nYour score was not added\n");
    }
    printf("\n==-==-==-=-==-==-==-==-==-==-==-==-==-==-==-==\n");
    printrank();

    free(game);
    return 0;
}


board *init(void){
    char *new[ROW][COL] = {{"01","02","03","04"},{"05","06","07","08"},{"09","10","11","12"},{"13","14","15","__"}};
    board *tabletop = malloc(sizeof(board));
    memcpy(tabletop->value, new, sizeof(new));
    srand(time(NULL));
    for (int i=0, x=rand()%(SCRAMBLE+1); i<x; i++){
        int dir = rand()%(4);
        tabletop = move(tabletop, dir);
    }
    tabletop->turns = 0;
    return tabletop;
}


board *move(board *game, int direction){
    char *cursor;
    int x = 0;
    int y = 0;
    do {
        cursor = game->value[x][y];
        if (strcmp(cursor, "__") != 0){
            x++;
            if (x == 4){
                x = 0;
                y++;
            }
        }
    } while (strcmp(cursor, "__") != 0);

    int directions[4][2] = {{-1,0}, {1,0}, {0,-1}, {0,1}};
    int new_x = x+directions[direction][0];
    int new_y = y+directions[direction][1];
    if (0 <= new_x && new_x <= 3 && 0 <= new_y && new_y <= 3){
            game->value[x][y] = game->value[new_x][new_y];
            game->value[new_x][new_y] = "__";
    }
    else{
        game->turns--;
    }

    return game;
}


bool checkwin(board *game){
    static const char *check[ROW][COL] = {{"01","02","03","04"},{"05","06","07","08"},{"09","10","11","12"},{"13","14","15","__"}};
    if (memcmp(game->value, check, sizeof(game->value)) == 0){
        return true;
    }
    return false;
}


int printboard(board *game){
    printf("\n%s %s %s %s\n%s %s %s %s\n%s %s %s %s\n%s %s %s %s\n\n",
    game->value[0][0],game->value[0][1],game->value[0][2],game->value[0][3],
    game->value[1][0],game->value[1][1],game->value[1][2],game->value[1][3],
    game->value[2][0],game->value[2][1],game->value[2][2],game->value[2][3],
    game->value[3][0],game->value[3][1],game->value[3][2],game->value[3][3]);

    return 1;
}

void next(board *game){
    //char dir[1];
    //printf("Input direction:\n0-Up, 1-Down, 2-Left, 3-Right\n");
    //fgets(dir, sizeof(dir), stdin);
    game -> turns++;
    printf("\n==-==-==-=-==-==-==-==-==-==-==-==-==-==-==-==\n");
    printf("\nTurn %i",game->turns);
    printboard(game);
    int dir = get_int("0-Up, 1-Down, 2-Left, 3-Right\n");
    game = move(game, dir);
}
