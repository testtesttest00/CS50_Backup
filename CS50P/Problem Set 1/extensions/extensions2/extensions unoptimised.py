def checkex(extype):
    return extype in ["gif", "jpg", "jpeg", "png", "pdf", "txt", "zip"]

def main():
    file = str(input("Enter file: ")).strip().lower()
    ext = str(getex(file))
    x = checkex(getex(file))

    if x == 1:
        if ext in["gif", "jpeg", "png"]:
            print("image/", ext, sep="")
        elif ext == "jpg":
            print("image/jpeg")
        elif ext in ["pdf","zip"]:
            print("application/", ext, sep="")
        else:
            print("text/plain")
    else:
        print("application/octet-stream")

def getex(full):
    name=full.rstrip("abcdefghijklmnopqrstuvwxyz")
    return str(full.removeprefix(name))

main()
