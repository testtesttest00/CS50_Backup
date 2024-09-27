import re
import sys

def main():
    print(count(str(input("Text: ")).strip()))

def count(s):
    um = re.findall(r"\bum\b", s, flags = re.IGNORECASE | re.ASCII)
    return len(um)

if __name__ == "__main__":
    main()
