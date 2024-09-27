from sys import argv, exit

def main():
    try:
        if len(argv) == 2:
            if argv[1].endswith(".py"):
                with open(argv[1], "r") as file:
                    print(countlines(file))
            else:
                exit
        elif 1:
            if len(argv) == 1:
                print("Too few command-line arguments")
            elif len(argv) > 2:
                print("Too many command-line arguments")
            exit
            # next time, try printing using sys.exit([arg])
    except OSError:
        print("File does not exist")
        exit

def countlines(file):
    lines = list(file)
    rm = 0
    ln = len(lines)
    for line in lines:
        if line.lstrip().startswith("#") or line.lstrip().startswith("\n") or line.strip() == "":
            rm += 1
    return ln - rm

if __name__ == "__main__":
    main()
