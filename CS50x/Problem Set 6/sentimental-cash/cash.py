import math

def main():
    while 1:
        try:
            change = float(input("Change: ").strip())
            if change < 0:
                raise Exception
            coins = [0.25, 0.10, 0.05, 0.01]
            i = 0
            for value in coins:
                i += math.floor(change / value)
                change = float("{:.2f}".format(change % value))
            print(f"{i}")
            break
        except (ValueError, Exception):
            pass

if __name__ == "__main__":
    main()
