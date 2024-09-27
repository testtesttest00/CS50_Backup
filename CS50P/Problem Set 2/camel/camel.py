def main():
    camel = str(input("camelCase: ")).strip()
    print("snake_case: ", snakify(camel))

def snakify(inp):
    for c in inp:
        if c.isupper() == 1:
            inp = inp.replace(c, "_" + c.lower())
    return inp

main()
