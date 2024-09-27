months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

def main():
    while 1:
        domini = newdate()
        if "/" in domini:
            mth, day, yr = domini.split("/")
            m = int(mth)
            d = int(day)
            if 0 < d < 31 and 0 < m < 13:
                print(yr, mth.zfill(2), day.zfill(2), sep = "-")
                break
        else:
            for i in range(12):
                if domini.startswith(months[i-1]):
                    dy = domini.removeprefix(months[i-1]).replace(" " , "")
                    day, yr = dy.split(",")
                    if int(day) < 1 or int(day) > 30:
                        break
                    mth = str(i)
                    print(yr, mth.zfill(2), day.zfill(2), sep = "-")
                    break
            if int(day) < 1 or int(day) > 30:
                newdate()
            else:
                break

def newdate():
    while 1:
        raw = str(input("Date: ")).strip().lower().capitalize()
        if "/" in raw and raw.replace("/", "").isnumeric():
            return raw
        elif "," in raw:
            for i in months:
                if raw.startswith(i) and raw.replace(",", "").replace(i, "").replace(" ", "").isnumeric():
                    return raw
# returned date will not be these erroneous inputs:
# 1) a/b/c (str in x/y/z)
# 2) 1 january 2021 (wrong format w/out ,)
# 3) 1 january, 2021 (wrong format w/ ,)
# 4) january asds 1, 2021 (any str w/ excess alphabets)

main()
