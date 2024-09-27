#include <cs50.h>
#include <stdio.h>
#include <math.h>

int digits(long num, int place);
int length(long num);
void raise(int type);
int luhn(long num);

int main(void){
    long card = get_long("Card: ");
    int l = length(card);
    if(l < 13 || l > 16){
        raise(0);
    }
    else if(l == 13 && digits(card, 13) == 4){
        raise(luhn(card)*2);
    }
    else if(l == 16){ // dont need length, if digits too high will be 0
        if(digits(card, 16) == 4){
            raise(luhn(card)*2);
        }
        else if(digits(card, 16) == 5){
            if(digits(card, 15) > 0 && digits(card, 15) < 6){
                raise(luhn(card)*3);
            }
            else{
                raise(0);
            }
        }
        else{
            raise(0);
        }
    }
    else if(l == 15 && digits(card, 15) == 3){ // dont need length == 15, if digits too high will be 0
        if(digits(card, 14) == 4 || digits(card, 14) == 7){
            raise(luhn(card)*4);
        }
        else{
            raise(0);
        }
    }
    else{
        raise(0);
    }
}


int digits(long num, int place){
    return num % (long)pow(10, place) / (long)pow(10,place-1);
}


int length(long num){
    int x = 0;
    while(num > 0) {
        num = num / 10;
        x ++;
    }
    return x;
}

void raise(int type){
    if(type == 0){
        printf("INVALID\n");
    }
    else if (type == 1){
        printf("INVALID\n");
    }
    else if (type == 2){
        printf("VISA\n");
    }
    else if (type == 3){
        printf("MASTERCARD\n");
    }
    else if (type == 4){
        printf("AMEX\n");
    }
}

int luhn(long num){
    int x = 0;
    for(int i = 2; i < 17; i = i + 2){
        int xx = 2 * digits(num, i);
        x = x + digits((long)xx, 1) + digits((long)xx, 2);
        printf("%i\n", x);
    }
    for(int j = 1; j < 16; j = j + 2){
        int y = digits(num, j);
        x = x + y;
        printf("%i\n", x);
    }
    if(digits(x, 1) == 0){
        return 1;
    }
    else{
        return 0;
    }
}
