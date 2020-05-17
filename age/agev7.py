def life_in_seconds():

    def age_in_seconds():
        text = birthdate
        new_text = text.split(',')
        month = int(new_text[0])
        day = int(new_text[1])
        year = int(new_text[2])

        if month == 1:
            month_in_seconds = 31536000
        if month == 2:
            month_in_seconds = 28857600
        if month == 3:
            month_in_seconds = 26438400
        if month == 4:
            month_in_seconds = 23760000
        if month == 5:
            month_in_seconds = 21168000
        if month == 6:
            month_in_seconds = 18489600
        if month == 7:
            month_in_seconds = 15897600
        if month == 8:
            month_in_seconds = 13219200
        if month == 9:
            month_in_seconds = 10540800
        if month == 10:
            month_in_seconds = 7948800
        if month == 11:
            month_in_seconds = 5270400
        if month == 12:
            month_in_seconds = 2678400

        day_in_seconds = day * 86400
        year_in_seconds = ((2020-year)*31536000)
        return (year_in_seconds+month_in_seconds-day_in_seconds)

    def this_year_in_seconds():
        text = nowdate
        date_text = text.split(',')
        new_month = int(date_text[0])
        new_day = int(date_text[1])

        now_day_in_seconds = new_day * 86400

        if new_month == 1:
            now_month_in_seconds = 0
        if new_month == 2:
            now_month_in_seconds = 2678400
        if new_month == 3:
            now_month_in_seconds = 5097600
        if new_month == 4:
            now_month_in_seconds = 7776000
        if new_month == 5:
            now_month_in_seconds = 10368000
        if new_month == 6:
            now_month_in_seconds = 13046400
        if new_month == 7:
            now_month_in_seconds = 15638400
        if new_month == 8:
            now_month_in_seconds = 18316800
        if new_month == 9:
            now_month_in_seconds = 20995200
        if new_month == 10:
            now_month_in_seconds = 23587200
        if new_month == 11:
            now_month_in_seconds = 26265600
        if new_month == 12:
            now_month_in_seconds = 28857600

        return (now_day_in_seconds + now_month_in_seconds)

    def leap_year_time():
        birthday = birthdate
        this_year = nowdate
        birth = birthday.split(',')
        birth_year = int(birth[2])
        birth_month = int(birth[0])
        year = this_year.split(',')
        now_year = int(year[2])
        now_month = int(year[0])

        if birth_year % 4 == 0 and birth_month < 3:
            leap_time = 86400
            new_birth_year = birth_year + 1
        if birth_year % 4 == 0 and birth_month >= 3:
            leap_time = 0
            new_birth_year = birth_year + 1
        if birth_year % 4 != 0:
            leap_time = 0
            new_birth_year = birth_year

        new_new_birth_year = 2020 - new_birth_year

        leap_days = new_new_birth_year // 4

        leap_times = leap_days * 86400

        if now_year % 4 == 0 and now_month < 3:
            this_leap_time = 0
        if now_year % 4 == 0 and now_month >= 3:
            this_leap_time = 86400
        if now_year % 4 != 0:
            this_leap_time = 0

        return leap_time + leap_times + this_leap_time

    def thousand_seperator(text):
        if len(text) == 6:
            return (f'{text[0:3]},{text[3:6]}')
        if len(text) == 7:
            return (f'{text[0]},{text[1:4]},{text[4:7]}')
        if len(text) == 8:
            return (f'{text[0:2]},{text[2:5]},{text[5:8]}')
        if len(text) == 9:
            return (f'{text[0:3]},{text[3:6]},{text[6:9]}')
        if len(text) == 10:
            return (f'{text[0]},{text[1:4]},{text[4:7]},{text[7:10]}')
        if len(text) == 11:
            return (f'{text[0:2]},{text[2:5]},{text[5:8]},{text[8:11]}')
        if len(text) == 12:
            return (f'{text[0:3]},{text[3:6]},{text[6:9]},{text[9:12]}')

    birthdate = str(input("What is your birthday? (ie. 2,5,1998)\n:"))
    nowdate = str(input("What is the date now? (ie. 9,12,2018)\n:"))

    age_seconds = age_in_seconds()
    this_year_seconds = this_year_in_seconds()
    this_leap_time = leap_year_time()

    time_in_seconds = str(age_seconds+this_leap_time+this_year_seconds)

    print(thousand_seperator(time_in_seconds))


life_in_seconds()
