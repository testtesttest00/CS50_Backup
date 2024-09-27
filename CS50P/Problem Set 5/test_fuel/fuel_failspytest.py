def main():
    fuel = str(input("Fraction: ")).strip()
    print(gauge(convert(fuel)))

def convert(fraction):
    num, denom = fraction.split("/")
    x = float(num)
    y = float(denom)
    try:
        if x > y:
            raise ValueError
        elif y == "0":
            raise ZeroDivisionError
        else:
            return int(round(x / y, 2)*100)
    except (ValueError, ZeroDivisionError):
        main()

def gauge(percentage):
    if percentage == None:
        pass
    elif percentage >= 99:
        raise "F"
    elif percentage <= 1:
        raise "E"
    else:
        raise f"{percentage}%"

if __name__ == "__main__":
    main()
