# Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
# Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
# Для простоты договоримся, что год может быть в диапазоне [1, 9999].
# Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
# Проверку года на високосность вынести в отдельную защищённую функцию.
#
# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.

import re


def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def is_valid_date(date):
    pattern = re.compile(r'^(\d{2})\.(\d{2})\.(\d{4})$')
    match = pattern.match(date)

    if not match:
        return False

    day = int(match.group(1))
    month = int(match.group(2))
    year = int(match.group(3))

    if month < 1 or month > 12:
        return False

    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 1 <= day <= 31
    elif month in [4, 6, 9, 11]:
        return 1 <= day <= 30
    else:
        return 1 <= day <= 29 if is_leap_year(year) else 1 <= day <= 28


if __name__ == "__main__":
    date = input("Введите дату в формате DD.MM.YYYY: ")

    if is_valid_date(date):
        print("Введенная дата существует.")
    else:
        print("Введенная дата невозможна.")

__all__ = ['is_valid_date']
