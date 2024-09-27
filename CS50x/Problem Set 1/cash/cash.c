#include <cs50.h>
#include <stdio.h>

int main(void){
    int cents;
    do{
        cents = get_int("Change owed: ");
    } while(cents<1);

    int coins = 0;
    if(cents % 25 != cents){
        int x = (cents-cents%25)/25;
        coins = coins + x;
        cents = cents - x * 25;
    }
    if(cents % 10 != cents){
        int x = (cents-cents%10)/10;
        coins = coins + x;
        cents = cents - x * 10;
    }
    if(cents % 5 != cents){
        int x = (cents-cents%5)/5;
        coins = coins + x;
        cents = cents - x * 5;
    }
    coins = coins + cents; // pennies
    printf("Coins: %i\n", coins);
}
