def main():
    greet = str(input("Hello there!\n")).strip().lower()
    print(f"${value(greet)}")


def value(greeting):
    greeting = greeting.strip().lower() #in function for testing purpose
    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("hello") == 0 and greeting.startswith("h"):
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()
