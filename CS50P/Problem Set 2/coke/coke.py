def main():
    cents = 0
    while cents < 50:
        print("Amount Due:", 50 - cents)
        add = int(input("Insert Coin: "))
        if add not in [5, 10, 25]:
            add = 0
        cents = cents + add
        if cents >= 50:
            print("Change Owed:", cents - 50)

main()
