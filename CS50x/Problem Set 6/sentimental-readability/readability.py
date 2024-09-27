import sys

def main():
    text = input("Text: ").strip()
    letters = 0.00
    words = 0.00
    sentences = 0.00
    pause = False
    for char in text:
        if char.isalnum():
            letters += 1
            pause = False
        elif char == " " and pause == False:
            words += 1
        elif char == ",":
            words += 1
            pause = True
        elif char in [".", "!", "?"]:
            words += 1
            sentences += 1
            pause = True
    coleman = round(0.0588 * (100 * (letters/words)) - 0.296 * (100 * (sentences/words)) - 15.8)
    if coleman < 1:
        print("Before Grade 1")
        sys.exit(0)
    elif coleman >= 16:
        print("Grade 16+")
        sys.exit(0)
    print(f"Grade {coleman}")


if __name__ == "__main__":
    main()
