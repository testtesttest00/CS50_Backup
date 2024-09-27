def convert(altered):
    print(altered.replace(":)", "🙂").replace(":(", "🙁"))

def main():
    x = str(input("How is yor day?\n"))
    convert(x)

main()
