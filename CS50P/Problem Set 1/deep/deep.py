def main():
    ans = str(input("What is the Answer to the Great Question of Life, the Universe, and Everything?\n")).strip().lower()
    check(ans)

def check(x):
    if x == "42" or x=="forty two" or x=="forty-two":
        print("Yes")
    else:
        print("No")

main()
