year = int(input("Enter a year \n"))
month = int(input("Enter a month \n"))


def leap_year(x):
    if x % 4 == 0:
        if x % 100 == 0:
            if x % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(y, m):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if leap_year(y) == True and m == 2:
        return 29
    return month_days[m - 1]


x = days_in_month(year, month)
print(f"Number of days {x}")
