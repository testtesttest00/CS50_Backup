def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if chklen(s)*chkspec(s) == 1:
        return chkstart(s)*chkseq(s)
    else:
        return 0

def chklen(s):
    return 1 < len(s) < 7

def chkstart(s):
    return (s[0]+s[1]).isalpha()

def chkspec(s):
    return s.isalnum()

def chkseq(s):
    i = 0
    j = 0
    while i < len(s):
        if s[i].isnumeric():
            j = i
            break
        elif s[i].isalpha() and i < len(s) - 1:
            i += 1
        elif s[i].isalpha() and i == len(s) - 1:
            return 1
    if s[j] == "0":
        return 0
    while j < len(s):
        if s[j].isalpha():
            return 0
        elif s[j].isnumeric() and j < len(s) - 1:
            j += 1
        elif s[j].isnumeric() and j == len(s) - 1:
            return 1
  # do checks only after trigger char

main()
