import sys
argv = sys.argv

def main():
    if len(argv) == 1:
        sys.exit()
    else:
        print("Adieu, adieu, to ", end = "")
        for i in argv[1 : -1]:
            print(i, ",", end = "")
        print("and", argv[len(argv) - 1])

main()
