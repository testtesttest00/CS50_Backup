def main():
    plate = str(input("Plate: "))
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if checklen(s) == 1:
        return checkstart(s)*checkalphanum(s)*checkspec(s)*checkzero(s)
    else:
        return 0

def checkstart(s):
    return str(s[0] + s[1]).isalpha()

def checklen(s):
    return 1<len(s)<7

# check alpha num error in cases eg CS50P2, CS50PP2, CS50PPP2 ...
def checkalphanum(s):
    i = 0
    while i < len(s):
        if s[i].isnumeric():
            j = i
            break
        elif i==len(s)-1 and s[i].isalpha():
            return 1
        else:
            i += 1
    if j != 0:
        while j < len(s):
            if s[j].isalpha():
                return 0
            elif j==len(s)-1 and s[j].isnumeric():
                return 1
            else:
                j += 1
    else:
        return 0


def checkspec(s):
    return s.isalnum()

def checkzero(s):
    i = 0
    j = 1
    while i < len(s):
        if s[i] == "0":
            j = 0
            break
        elif s[i].isnumeric():
            break
        else:
            i += 1
    return j

main()
