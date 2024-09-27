def main():
     inp = str(input("What time is it? ")).strip()
     con = convert(inp)
     comparison(con)

def convert(time):
    hr, minu = time.split(":")
    total = float(hr) + float(minu)/60
    return round(total, 2)

def comparison(hr24):
    if 7 <= hr24 <= 8:
        print("breakfast time")
    elif 12 <= hr24 <= 13:
        print("lunch time")
    elif 18 <= hr24 <= 19:
        print("dinner time")

if __name__ == "__main__":
    main()
