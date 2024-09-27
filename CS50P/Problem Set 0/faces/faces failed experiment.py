def convert(unaltered):
    altered = unaltered.replace(":)", "🙂").replace(":(", "🙁")
    main(altered)

def main(y):
    x = str(input("How is yor day?\n"))
    convert(x)
    print(y)

main(0)
