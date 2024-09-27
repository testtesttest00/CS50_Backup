def main():
    fuel = str(input("Fraction: ")).strip()
    print(gauge(convert(fuel)))

def convert(fraction):
    num, denom = fraction.split("/")
    x = float(num)
    y = float(denom)
    if y == 0:
        raise ZeroDivisionError
    elif x > y:
        raise ValueError
    else:
        return int(round(x / y, 2)*100)

def gauge(percentage):
    if percentage == None:
        pass
    elif percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()
