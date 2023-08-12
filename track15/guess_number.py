# Создайте модуль с функцией внутри.
# Функция принимает на вход три целых числа: нижнюю и верхнюю границу и количество попыток.
# Внутри генерируется случайное число в указанных границах и пользователь должен угадать его за заданное число попыток.
# Функция выводит подсказки “больше” и “меньше”.
# Если число угадано, возвращается истина, а если попытки исчерпаны - ложь.
# Добавьте возможность запуска функции “угадайки” из модуля в командной строке терминала.
# Строка должна принимать от 1 до 3 аргументов: параметры вызова функции.
# Для преобразования строковых аргументов командной строки в числовые параметры используйте генераторное выражение.

import random
import sys

def guess_number(lower_bound, upper_bound, attempts):
    number_to_guess = random.randint(lower_bound, upper_bound)

    for attempt in range(attempts):
        guess = int(input("Введите вашу догадку: "))

        if guess > number_to_guess:
            print("Ваше число больше загаданного.")
        elif guess < number_to_guess:
            print("Ваше число меньше загаданного.")
        else:
            print("Поздравляем! Вы угадали число!")
            return True

    print("К сожалению, попытки исчерпаны. Загаданное число:", number_to_guess)
    return False

# Список функций, доступных из модуля
__all__ = ['guess_number']

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Использование: python guess_number.py <нижняя_граница> <верхняя_граница> <количество_попыток>")
    else:
        lower_bound = int(sys.argv[1])
        upper_bound = int(sys.argv[2])
        attempts = int(sys.argv[3])
        guess_number(lower_bound, upper_bound, attempts)
