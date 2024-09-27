from PIL import Image, ImageOps
from sys import argv, exit

def main():
    if len(argv) < 3:
        exit("Too few command-line arguments")
    elif len(argv) > 3:
        exit("Too many command-line arguments")
    elif "." in argv[1] and "." in argv[2]:
        name1, ext1 = argv[1].rsplit(".")
        name2, ext2 = argv[2].rsplit(".")
        if ext1 in ["jpg", "jpeg", "png"]:
            if ext1 == ext2:
                try:
                    with Image.open(argv[1]) as img:
                        image(img, argv[2])
                except FileNotFoundError:
                    exit("File does not exist")
            else:
                exit("Must be same file type")
        else:
            exit("Invalid file type")
    else:
        exit("Invalid file type")

def image(inp, out):
    with Image.open("shirt.png") as shirt:
        fittedimg = ImageOps.fit(inp, shirt.size)
        fittedimg.paste(shirt, shirt)
        fittedimg.save(out)

if __name__ == "__main__":
    main()
