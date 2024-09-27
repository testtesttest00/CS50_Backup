def main():
    file = str(input("File name: ")).lower().strip()
    process(getext(file))

def getext(full):
    name, ext = full.rsplit(".", 1)
    return ext

def process(ext):
    if ext == "gif":
        print("image/gif")
    elif ext in ["jpg", "jpeg"]:
        print("image/jpeg")
    elif ext == "png":
        print("image/png")
    elif ext == "pdf":
        print("application/pdf")
    elif ext == "zip":
        print("application/zip")
    elif ext == "txt":
        print("text/plain")
    else:
        print("application/octet-stream")

main()
