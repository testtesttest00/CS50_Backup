def main():
    i = input("Height: ").strip()
    while 1:
        try:
            i = int(i)
            if i < 1 or i > 8:
                raise Exception
            x = i
            while i != 0:
                print((i-1)*" " + (x-(i-1))*"#" + "  " + (x-(i-1))*"#", sep = "", end = "\n")
                i -= 1
            break
        except:
            print("Input an integer between 1 and 8.")
            i = input("Height: ").strip()

if __name__ == "__main__":
    main()
