from PIL import Image, ImageOps
from sys import argv, exit
import os

def main():
    if len(argv) < 3:
        exit("Too few command-line arguments")
    elif len(argv) > 3:
        exit("Too many command-line arguments")
    else:
        root1, ext1 = os.path.splitext(argv[1])
        root2, ext2 = os.path.splitext(argv[2])
        if ext1 in [".jpg", ".jpeg", ".png"]:
            if ext1 == ext2:
                try:
                    with Image.open(argv[1]) as img:
                        image(img, argv[2])
                except FileNotFoundError:
                    exit("File does not exist")
            else:
                exit("File types are different")
        else:
            exit("Invalid file type")

def image(inp, out):
    with Image.open("shirt.png") as shirt:
        fittedimg = ImageOps.fit(inp, shirt.size)
        fittedimg.paste(shirt, shirt)
        fittedimg.save(out)

if __name__ == "__main__":
    main()
