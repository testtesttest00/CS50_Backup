def main():
    file = str(input("File name: ").strip().lower())
    if checkimage(file) == 1:
        print(checkimage(file))
    elif checkimage(file) == 0 and checkapp(file) == 1:
        print(checkapp(file))
    elif file.endswith(".txt") == 1:
        print("plain/text")
    else:
        print("application/octet-stream")

def checkimage(full):
    return full.endswith(".gif", ".jpg", ".jpeg")
    if full.endswith(".gif") == 1:
        return("image/gif")
    elif full.endswith(".jpg", ".jpeg") == 1:
        return("image/jpeg")
    else:
        return("image/png")

def checkapp(full):
    return full.endswith(".pdf", ".zip")
    if full.endwith(".pdf") == 1:
        return("application/pdf")
    else:
        return("application/zip")

main()
