# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.


import sys


def _is_leap(year):
    return bool(not year % 4 and year % 100 or not year % 400)


def check_date(date):
    MONTH = [31, (28, 29), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day, month, year = list(map(int, date))
    if 0 < year < 9999:
        if month == 2:
            return bool(0 < day <= (MONTH[month - 1][1] if _is_leap(year) else MONTH[month - 1][0]))
        else:
            if 0 < month < 13:
                return 0 < day <= MONTH[month - 1]


if __name__ == '__main__':
    date = sys.argv[-1].split('.')
    print(check_date(date))

