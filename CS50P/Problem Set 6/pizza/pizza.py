import csv
from tabulate import tabulate
from sys import argv, exit

def main():
    menulist = []
    if len(argv) == 1:
        exit("Too few command-line arguments")
    elif len(argv) > 2:
        exit("Too many command-line arguments")
    elif argv[1].endswith(".csv") == 0:
        exit("Not a csv file")
    else:
        try:
            with open(argv[1], "r") as file:
                menu = csv.reader(file, quotechar = ",")
                for _ in menu:
                    menulist.append(_)
                print(tabulate(menulist, headers = "firstrow", tablefmt = "grid"))
        except FileNotFoundError:
            exit("File not found")

if __name__ == "__main__":
    main()
