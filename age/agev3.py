def age_in_seconds(text):
    newbirth = text.split(',')
    newnewbirth = int(newbirth[0])
    newnewnewbirth = int(newbirth[1])
    newnewnewnewbirth = int(newbirth[2])
    if newnewbirth == 1:
        month_in_seconds = 0
    if newnewbirth == 2:
        month_in_seconds = 2678400
    if newnewbirth == 3:
        month_in_seconds = 5097600
    if newnewbirth == 4:
        month_in_seconds = 7776000
    if newnewbirth == 5:
        month_in_seconds = 10368000
    if newnewbirth == 6:
        month_in_seconds = 13046400
    if newnewbirth == 7:
        month_in_seconds = 15638400
    if newnewbirth == 8:
        month_in_seconds = 18316800
    if newnewbirth == 9:
        month_in_seconds = 20995200
    if newnewbirth == 10:
        month_in_seconds = 23587200
    if newnewbirth == 11:
        month_in_seconds = 26265600
    if newnewbirth == 12:
        month_in_seconds = 28857600
    day_in_seconds = newnewnewbirth * 86400
    year_in_seconds = (2020-newnewnewnewbirth)*31557600
    return year_in_seconds + day_in_seconds + month_in_seconds


text = input("What is your birthday? (ie. 10,16,1968)\n:")
print(age_in_seconds(text))
