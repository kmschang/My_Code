
def seconds_old():
    secinday = 86400
    secinyear = 31536000
    year = int(input("What year were you born in?\n:"))
    yearold = (2020 - year)*secinyear

    month = int(input("What month were you born?\n:"))
    if month == 1:
        monthdays = 0
    if month == 2:
        monthdays = 31
    if month == 3:
        monthdays = 59
    if month == 4:
        monthdays = 90
    if month == 5:
        monthdays = 120
    if month == 6:
        monthdays = 151
    if month == 7:
        monthdays = 181
    if month == 8:
        monthdays = 212
    if month == 9:
        monthdays = 243
    if month == 10:
        monthdays = 273
    if month == 11:
        monthdays = 304
    if month == 12:
        monthdays = 334
    monthold = monthdays * secinday

    day = int(input("What day of the month were you born?\n:"))
    dayold = day * secinday

    secold = yearold + monthold + dayold

    return (secold)


print(seconds_old())


def minutes_old():
    secinday = 86400
    secinyear = 31536000
    year = int(input("What year were you born in?\n:"))
    yearold = (2020 - year)*secinyear

    month = int(input("What month were you born?\n:"))
    if month == 1:
        monthdays = 0
    if month == 2:
        monthdays = 31
    if month == 3:
        monthdays = 59
    if month == 4:
        monthdays = 90
    if month == 5:
        monthdays = 120
    if month == 6:
        monthdays = 151
    if month == 7:
        monthdays = 181
    if month == 8:
        monthdays = 212
    if month == 9:
        monthdays = 243
    if month == 10:
        monthdays = 273
    if month == 11:
        monthdays = 304
    if month == 12:
        monthdays = 334
    monthold = monthdays * secinday

    day = int(input("What day of the month were you born?\n:"))
    dayold = day * secinday

    secold = yearold + monthold + dayold
    minold = secold / 60
    return int((minold))


print(minutes_old())
