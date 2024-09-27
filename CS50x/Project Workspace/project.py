import subprocess


def main():
    print("\n==-==-==-=-==-==-==-==-==-==-==-==-==-==-==-==\n")
    while 1:
        run = input(\
"Choose Version to Run:\n\
1) C\n\
2) Python\n\
3) HTML (Flask)\n\
Recommended: C > Python > HTML (Flask)\n\n").strip().lower()
        if run in ["1", "c", "2", "python", "3", "html", "flask", "html (flask)"]:
            break
        print("\n==-==-==-=-==-==-==-==-==-==-==-==-==-==-==-==\n\nEnter 1, 2 or 3 only\n")
        pass
    print("\n==-==-==-=-==-==-==-==-==-==-==-==-==-==-==-==\n\nRunning...")
    if run in ["1", "c"]:
        subprocess.run(["make", "cver"], cwd="./versions/cver")
        subprocess.run(["./cver"], cwd="./versions/cver")
    if run in ["2", "python"]:
        subprocess.run(["python", "versions/pver.py"])
    if run in ["3", "html", "flask", "html (flask)"]:
        subprocess.run(["flask", "run"], cwd="versions/hver")


if __name__ == "__main__":
    main()
