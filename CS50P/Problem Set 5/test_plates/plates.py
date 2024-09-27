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
        if j == 1 and s[i].isalpha():
            return 0
        #post-numeric
        elif j == 0 and s[i] == "0":
            return 0
        elif s[i].isnumeric() - j and i < len(s) - 1:
            j = bool(s[i].isnumeric)
            i += 1
        #ini: leaves alphabets
        #catches 1st numeric, continue loop
        #aft: leaves num
        elif s[i].isnumeric() - j and i == len(s) - 1:
            return 1
        elif s[i].isalpha() + j and i < len(s) - 1:
            i += 1
        elif s[i].isalpha() + j and i == len(s) - 1:
            return 1
  # do checks only after trigger char

if __name__ == "__main__":
    main()
