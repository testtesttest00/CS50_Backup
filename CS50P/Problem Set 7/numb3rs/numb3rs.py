import re
import sys

def main():
    print(validate(str(input("IPv4 Address: ")).strip()))

def validate(ip):
    r = list(range(256))
    no = []
    if x := re.fullmatch(r"(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})", ip, re.ASCII):
        for _ in x.groups():
            no.append(int(_))
        return bool((no[0] in r)*(no[1] in r)*(no[2] in r)*(no[3] in r))
    else:
        return False

#    return bool(re.fullmatch(r"[0-255](\.[0.255])", ip))
#mistake: [0-255] was used. error: re tests each char individually, hence only [0-9] is recognise.
#[0-255] was read as [0-2]

if __name__ == "__main__":
    main()
