from random import randint
from sys import exit

def main():
    while 1:
        try:
            n = int(input("Level: "))
            if n > 0:
                break
        except ValueError:
            main()
    ans = randint(1, n)
    while 1:
        try:
            guess = int(input("Guess: "))
            if guess > 0:
                if guess < ans:
                    print("Too small!")
                elif guess > ans:
                    print("Too large!")
                elif guess == ans:
                    print("Just right!")
                    exit()
        except ValueError:
            pass

main()
