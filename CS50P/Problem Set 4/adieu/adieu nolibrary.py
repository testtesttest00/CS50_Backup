import inflect
p = inflect.engine()

names = []
def main():
    try:
        while 1:
            names.append(str(input("Name: ").strip()))
    except EOFError:
        f = 1
        if len(names) < 3:
            f = 0
        print("\nAdieu, adieu, to ", end = "")
        for i in names[0 : -2]:
            print(i, ", ", end = "", sep = "")
        if len(names) > 1:
            print(names[len(names) - 2], f*",", " and ", names[len(names) - 1], sep ="")
        else:
            print(names[0])

main()
