from random import randint

def main():
    score = 0
    lvl = get_level()
    for i in range(10):
        x = generate_integer(lvl)
        y = generate_integer(lvl)
        for attempts in range(4):
            if attempts == 3:
                print(x, "+", y, "=", x+y)
                break
            print(x, "+", y, "=")
            ans = str(input()).strip()
            if ans == str(x + y):
                score += 1
                i += 1
                break
            else:
                print("EEE")
                attempts += 1
    print(f"Score: {score}")

def get_level():
    while 1:
        try:
            lvl = int(input("Level: ").strip())
            if lvl in [1, 2, 3]:
                return lvl
        except ValueError:
            pass

def generate_integer(level):
    try:
        if level not in [1, 2, 3]:
            raise ValueError
    except ValueError:
        get_level()
    if level == 1:
        return randint(0,9)
    elif level == 2:
        return randint(10,99)
    else:
        return randint(100,999)

if __name__ == "__main__":
    main()
