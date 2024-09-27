import inflect
p = inflect.engine()

def main():
    namelist = []
    while 1:
        try:
            namelist.append(str(input("Name: ")).strip())
        except EOFError:
            print("Adieu, adieu, to", p.join(namelist))
            break

main()
