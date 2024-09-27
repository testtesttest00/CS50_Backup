def main():
    inp = str(input("Input: "))
    print("Output:", shorten(inp))

def shorten(text):
    for c in text:
        if c.lower() in ["a", "e", "i", "o", "u"]:
            text = text.replace(c, "")
    return text

if __name__ == "__main__":
    main()
