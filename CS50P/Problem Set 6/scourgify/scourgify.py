import csv
from sys import argv, exit

def main():
    if len(argv) > 3:
        exit("Too many command-line arguments")
    elif len(argv) < 3:
        exit("Too few command-line arguments")
    elif argv[1].endswith(".csv") == 0 or argv[2].endswith(".csv") == 0:
        exit("Invalid file type")
    else:
        try:
            with open(argv[1]) as bef:
                conv(bef, argv[2])
        except FileNotFoundError:
            exit(f"Could not read {argv[1]}")

def conv(bef, aft):
    finallist = []
    befdict_obj = csv.DictReader(bef)
    for full in befdict_obj:
        last, first = full["name"].split(", ")
        finallist.append([first, last, full["house"]])
        with open(aft, "w") as after:
            aftcsv_obj = csv.writer(after)
            aftcsv_obj.writerow(["first" ,"last", "house"])
            aftcsv_obj.writerows(finallist)

if __name__ == "__main__":
    main()
