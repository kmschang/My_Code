def age_in_seconds(text):
    newbirth = text.split(",")
    newnewbirth = int(newbirth[0])
    newnewnewbirth = int(newbirth[1])
    newnewnewnewbirth = int(newbirth[2])

    if newnewbirth == 1:
        month_in_seconds = 28857600
    if newnewbirth == 2:
        month_in_seconds = 26265600
    if newnewbirth == 3:
        month_in_seconds = 23587200
    if newnewbirth == 4:
        month_in_seconds = 20995200
    if newnewbirth == 5:
        month_in_seconds = 18316800
    if newnewbirth == 6:
        month_in_seconds = 15638400
    if newnewbirth == 7:
        month_in_seconds = 13046400
    if newnewbirth == 8:
        month_in_seconds = 10368000
    if newnewbirth == 9:
        month_in_seconds = 7776000
    if newnewbirth == 10:
        month_in_seconds = 5097600
    if newnewbirth == 11:
        month_in_seconds = 2678400
    if newnewbirth == 12:
        month_in_seconds = 0
    day_in_seconds = newnewnewbirth * 86400
    year_in_seconds = (2020 - newnewnewnewbirth) * 31557600

    date = input("What is the date? (ie. 1,26,1999(full year))\n:")
    nowdate = date.split(",")
    nownowdate = int(nowdate[0])
    nownownowdate = int(nowdate[1])
    nownownownowdate = int(nowdate[2])
    if nownownowdate == 29 and nownowdate == 2:
        leap_chance = True
    else:
        leap_chance = False
    if nownownownowdate % 4 == 0 and nownowdate >= 3:
        leap_time = 86400
    if leap_chance == True:
        leap_time = 86400
    else:
        leap_time = 0

    if nownowdate == 1:
        now_month_in_seconds = 0
    if nownowdate == 2:
        now_month_in_seconds = 2678400
    if nownowdate == 3:
        now_month_in_seconds = 5097600
    if nownowdate == 4:
        now_month_in_seconds = 7776000
    if nownowdate == 5:
        now_month_in_seconds = 10368000
    if nownowdate == 6:
        now_month_in_seconds = 13046400
    if nownowdate == 7:
        now_month_in_seconds = 15638400
    if nownowdate == 8:
        now_month_in_seconds = 18316800
    if nownowdate == 9:
        now_month_in_seconds = 20995200
    if nownowdate == 10:
        now_month_in_seconds = 23587200
    if nownowdate == 11:
        now_month_in_seconds = 26265600
    if nownowdate == 12:
        now_month_in_seconds = 28857600
    now_day_in_seconds = nownownowdate * 86400

    this_year_age = now_month_in_seconds + now_day_in_seconds

    age = str(
        year_in_seconds + month_in_seconds + day_in_seconds + this_year_age + leap_time
    )

    reverse_age = age[::-1]
    if len(reverse_age) == 10:
        thousand_seperator = f"{reverse_age[0:3]},{reverse_age[3:6]},{reverse_age[6:9]},{reverse_age[9:12]}"
    else:
        thousand_seperator = f"{reverse_age[0:3]},{reverse_age[3:6]},{reverse_age[6:9]}"
    final = thousand_seperator[::-1]
    return final


text = input("What is your birthday? (ie. 1,26,1968(full year))\n:")
print(age_in_seconds(text))
