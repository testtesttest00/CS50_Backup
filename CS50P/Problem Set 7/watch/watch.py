import re
import sys

def main():
    print(parse(str(input("HTML: ")).strip()))

def parse(s):
    link = re.fullmatch(
        r"<iframe src=\"https?://(?:www\.)?youtube\.com/embed/(\w+)\"></iframe>",
        s,
        re.IGNORECASE)
    if link:
        return f"https://youtu.be/{link.group(1)}"
    else:
        return None

if __name__ == "__main__":
    main()
