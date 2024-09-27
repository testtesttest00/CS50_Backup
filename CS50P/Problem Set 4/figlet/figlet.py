from pyfiglet import Figlet
figlet = Figlet()
import sys
import random

valid_fonts = list(figlet.getFonts())

def invalid():
    sys.exit("Invalid Usage")

def printer():
    print("Output: \n", figlet.renderText(str(input("Input: ")).strip()))

def main():
    if len(sys.argv) == 3:
        if sys.argv[1] in ["-f", "--font"] and sys.argv[2] in valid_fonts:
            figlet.setFont(font = sys.argv[2])
            printer()
        else:
            invalid()
    elif len(sys.argv) == 1:
        figlet.setFont(font = random.choice(valid_fonts))
        printer()
    else:
        invalid()

main()
