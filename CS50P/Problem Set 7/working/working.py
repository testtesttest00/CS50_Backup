import re
import sys

def main():
    print(convert(str(input("Hours: ")).strip()))

def convert(s):
    time = re.fullmatch(r"(\d{1,2}):?(\d\d)? ([AP]M) to (\d{1,2}):?(\d\d)? ([AP]M)", s)
    if time:
    #shortens time.group into t
        t =["blank"]
        for _ in time.groups():
            t.append(_)
    #rejects invalid hours value
        if int(t[1])>12 or int(t[1])<0 or int(t[4])>12 or int(t[4])<0:
            raise ValueError
    #converts 12hr to 24hr, including special case with hr = 12
        if t[3] == "PM":
            t[1] = str(int(t[1]) + 12)
        if t[6] == "PM":
            t[4] = str(int(t[4]) + 12)
        if t[1] == "12" or t[1] == "24":
            t[1] = str(int(t[1]) - 12)
        if t[4] == "12" or t[4] == "24":
            t[4] = str(int(t[4]) - 12)
    #convert None into 00
        if t[2] == None:
            t[2] = "00"
        if t[5] == None:
            t[5] = "00"
    #rejects invalid minutes value
        if int(t[2])>59 or int(t[2])<0 or int(t[5])>59 or int(t[5])<0:
            raise ValueError
    #return
        return f"{t[1].zfill(2)}:{t[2]} to {t[4].zfill(2)}:{t[5]}"
    else:
        raise ValueError

if __name__ == "__main__":
    main()

# (\d):?(\d\d)? ([AP]M) to (\d):?(\d\d)? ([AP]M)
