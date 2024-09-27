import emoji

def main():
    inp = str(input("Input: ")).lower().strip()
    print(emoji.emojize(inp, language = "alias"))

main()
