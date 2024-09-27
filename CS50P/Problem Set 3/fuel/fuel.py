def main():
    while 1:
        try:
            frac = str(input("Fraction: ")).strip()
            numer, denom = frac.split("/")
            if int(numer) <= int(denom):
                perc = float(int(numer)/int(denom))*100
                break
        except ValueError:
            pass
        except ZeroDivisionError:
            pass
    if perc <= 1:
        print("E")
    elif perc >= 99:
        print("F")
    else:
        print(round(perc),"%",sep="")

main()
