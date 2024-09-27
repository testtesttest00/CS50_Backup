def main():
    inp = str(input("What time is it? ")).strip()
    conv = convert(inp)
    if 7 <= conv <= 8:
        print("breakfast time")
    elif 12 <= conv <= 13:
        print("lunch time")
    elif 18 <= conv <= 19:
        print("dinner time")

def convert(time):
    hr, minu = time.split(":")
    if minu.endswith("p.m."):
        rminu = minu.removesuffix(" p.m.")
        pm24 = float(hr) + 12
        total = pm24 + float(rminu)/60
    elif minu.endswith("a.m."):
        rminu = minu.removesuffix(" a.m.")
        total = float(hr) + float (rminu)/60
    else:
        total = float(hr) + float(minu)/60
    return total

if __name__ == "__main__":
    main()
