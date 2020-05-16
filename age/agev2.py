def age_in_seconds():
    while True:
        year = int(input("What year were you born in?\n:"))
        if year > 2020:
            print("Please put the real year. Thank you.")
        else:
            year_in_seconds = (2020-year)*31557600
            break
    while True:
        month = int(input("What month were you born in? (number)\n:"))
        if month == 1:
            month_in_seconds = 0
            break
        if month == 2:
            month_in_seconds = 2678400
            break
        if month == 3:
            month_in_seconds = 5097600
            break
        if month == 4:
            month_in_seconds = 7776000
            break
        if month == 5:
            month_in_seconds = 10368000
            break
        if month == 6:
            month_in_seconds = 13046400
            break
        if month == 7:
            month_in_seconds = 15638400
            break
        if month == 8:
            month_in_seconds = 18316800
            break
        if month == 9:
            month_in_seconds = 20995200
            break
        if month == 10:
            month_in_seconds = 23587200
            break
        if month == 11:
            month_in_seconds = 26265600
            break
        if month == 12:
            month_in_seconds = 28857600
            break

    day = int(input("What day of the month were you born?\n:"))
    day_in_seconds = day * 86400


    return year_in_seconds + month_in_seconds + day_in_seconds


print(age_in_seconds())
