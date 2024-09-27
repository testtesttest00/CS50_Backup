months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

def newdate():
    raw = str(input("Date: ")).strip().lower().capitalize()
    while 1:
        if "/" in raw and raw.replace("/", "").isnumeric():
            return raw
        elif "," in raw:
            for i in months:
                if raw.startswith(i) and raw.removeprefix(i).replace(",", "").replace(" ", "").isnumeric():
                    return raw

def main():
    while 1:
        date = newdate()
        try:
            mth, day, yr = date.split("/")
            if 0<int(mth)<13 and 0<int(day)<30:
                print(yr, mth.zfill(2), day.zfill(2), sep ="-")
                break
        except ValueError:
            for i in range(12):
                if months[i] in date and "," in date:
                    dy = date.removeprefix(months[i]).replace(" ", "")
                    day, year = dy.split(",")
                    break
            if int(day) - 1 in range(29):
                print(year, str(i + 1).zfill(2), day.zfill(2), sep = "-")
                break

main()
