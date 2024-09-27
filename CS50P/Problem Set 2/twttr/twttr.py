def main():
    inp = str(input("Input: "))
    print("Output:", devowel(inp))

def devowel(text):
    for c in text:
        if c.lower() in ["a", "e", "i", "o", "u"]:
            text = text.replace(c, "")
    return text
main()
