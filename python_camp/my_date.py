class MyDate:

    def __init__(self, year=0, month=0, day=0, hour=0, minute=0, sec=0):

        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.sec = sec
        if not year == 0 and month == 0 and day == 0:
            self.error_date(self.year, self.month, self.day, self.hour, self.minute, self.sec)
    def error_date(self, year, month, day, hour, minute, sec):
        if year < 1:
            raise ValueError("에러_year")
        if month < 1 or month > 12:
            raise ValueError("에러_month")
        if day < 1 or day > self.days_in_month(year, month):
            raise ValueError("에러_day")
        if hour < 0 or hour >= 24:
            raise ValueError("에러_hour")
        if minute < 0 or minute >= 59:
            raise ValueError("에러_minute")
        if sec < 0 or sec > 59:
            raise ValueError("에러_sec")
        if sec == 60 and (minute != 59 or hour != 23):
            raise ValueError("에러_sec")
        return True

    def days_in_month(self, year, month):
        if month in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        if month in [4, 6, 9, 11]:
            return 30
        if month == 2:
            return 29 if self.yoon_year(year) else 28
        return True
    def yoon_year(self, year):
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    def __add__(self, other):
        add_year = self.year + other.year
        add_month = self.month + other.month
        add_day = self.day + other.day
        add_hour = self.hour + other.hour
        add_minute = self.minute + other.minute
        add_sec = self.sec + other.sec

        if add_sec >= 60:
            add_minute += add_sec // 60
            add_sec %= 60
        if add_minute >= 60:
            add_hour += add_minute // 60
            add_minute %= 60
        if add_hour >= 24:
            add_day += add_hour // 24
            add_hour %= 24
        if add_month > 12:
            add_year += add_month // 12
            add_month %= 12
        while add_day > self.days_in_month(add_year, add_month):
            add_day -= self.days_in_month(add_year, add_month)
            add_month += 1
            if add_month > 12:
                add_month = 1
                add_year += 1
        return MyDate(add_year, add_month, add_day, add_hour, add_minute, add_sec)
    def __sub__(self, other): #mydate끼리 빼는
        sub_year = self.year - other.year
        sub_month = self.month - other.month
        sub_day = self.day - other.day
        sub_hour = self.hour - other.hour
        sub_minute = self.minute - other.minute
        sub_sec = self.sec - other.sec
        if sub_sec < 0:
            sub_minute -= 1
            sub_sec += 60
        if sub_minute < 0:
            sub_hour -= 1
            sub_minute += 60
        if sub_hour < 0:
            sub_day -= 1
            sub_hour += 24
        if sub_day <= 0:
            sub_month -= 1
            if sub_month == 0:
                sub_year -= 1
                sub_month = 12
            sub_month_days = self.days_in_month(sub_year, sub_month)
            if sub_day != -1:
                sub_day += sub_month_days
            else:
                sub_day = sub_month_days

            while sub_day > self.days_in_month(sub_year, sub_month):
                sub_day -= self.days_in_month(sub_year, sub_month)
                sub_month += 1
                if sub_month > 12:
                    sub_year += 1
                    sub_month = 1

        return MyDate(sub_year, sub_month, sub_day, sub_hour, sub_minute, sub_sec)

    def __eq__(self, other):
        return (self.year == other.year and
                self.month == other.month and
                self.day == other.day and
                self.hour == other.hour and
                self.minute == other.minute and
                self.sec == other.sec)

    def __lt__(self, other):
        if self.year != other.year:
            return self.year < other.year
        if self.month != other.month:
            return self.month < other.month
        if self.day != other.day:
            return self.day < other.day
        if self.hour != other.hour:
            return self.hour < other.hour
        if self.minute != other.minute:
            return self.minute < other.minute
        return self.sec < other.sec

    def __le__(self, other): # d1<=d2
        return self.__eq__(other) or self.__lt__(other)

    def __gt__(self, other):
        return not self.__le__(other)

    def __ge__(self, other):
        return not self.__lt__(other)

    def __str__(self):
        return f"{self.year}-{self.month:01d}-{self.day:01d} {self.hour:01d}:{self.minute:01d}:{self.sec:01d}"


if __name__ == '__main__':

    d0 = MyDate()
    d1 = MyDate(2022, 1, 31, 14, 30)
    try:
        d2 = MyDate(2024, 8, 100, 23, 10)
    except ValueError as e:
        print(e)
    try:
        d3 = MyDate(2024, 2, 30)
    except ValueError as e:
        print(e)
    print("============================================================")
    d3 = MyDate(day=31)
    # assert d1 + d3 == MyDate(2022, 4, 2, 14, 30)
    # assert d1 - d3 == MyDate(2022, 3, 31, 14, 30)

    result = d1 + d3
    result2 = d1 - d3
    expected = MyDate(2022, 4, 2, 14, 30)
    expected2 = MyDate(2022, 3, 31, 14, 30)
    print(f"날짜 플러스: {result}")
    print()
    print(f"날짜 마이너스: {result2}")
    print()

    assert d1 < d2

    result3 = d1 < d2
    result4 = d1 <= d2
    result5 = d1 > d2
    result6 = d1 == d2
    print(f'1) d1 < d2 : {result3}')
    print(f'2) d1 <= d2 : {result4}')
    print(f'3) d1 > d2 : {result5}')
    print(f'4) d1 == d2 : {result6}')
    print("============================================================")