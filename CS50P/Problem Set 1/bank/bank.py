def checkh(greet):
    return greet.startswith("h")

def checkhello(hello):
    return hello.startswith("hello")

def main():
    talk = str(input("Hello there!\n").strip().lower())
    if checkh(talk) == 1:
        if checkhello(talk) == 1:
            print("$0")
        else:
            print("$20")
    else:
        print("$100")

main()
