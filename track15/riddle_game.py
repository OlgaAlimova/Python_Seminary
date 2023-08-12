# Создайте модуль с функцией внутри.
# Функция получает на вход загадку, список с возможными вариантами отгадок и количество попыток на угадывание.
# Программа возвращает номер попытки, с которой была отгадана загадка или ноль, если попытки исчерпаны.
#
# Добавьте в модуль с загадками функцию, которая хранит словарь списков.
# Ключ словаря - загадка, значение - список с отгадками.
# Функция в цикле вызывает загадывающую функцию, чтобы передать ей все свои загадки.
#
# Добавьте в модуль с загадками функцию, которая принимает на вход строку (текст загадки) и число (номер попытки, с которой она угадана).
# Функция формирует словарь с информацией о результатах отгадывания.
# Для хранения используйте защищённый словарь уровня модуля.
# Отдельно напишите функцию, которая выводит результаты угадывания из защищённого словаря в удобном для чтения виде.
# Для формирования результатов используйте генераторное выражение.

import random

# Защищенный словарь для хранения результатов отгадывания
_results = {}

def guess_riddle(riddle, options, attempts):
    print("Загадка:", riddle)
    print("Варианты ответов:", options)

    correct_answer = random.choice(options)

    for attempt in range(1, attempts + 1):
        guess = input(f"Попытка {attempt}: Ваш ответ: ")

        if guess == correct_answer:
            print("Поздравляем! Вы угадали загадку с попытки", attempt)
            _results[riddle] = attempt
            return attempt

    print("К сожалению, попытки исчерпаны. Правильный ответ:", correct_answer)
    _results[riddle] = 0
    return 0

def show_results():
    print("\nРезультаты угадывания загадок:")
    for riddle, attempt in _results.items():
        result = "Угадано с попытки" if attempt > 0 else "Не угадано"
        print(f"Загадка: {riddle}, Результат: {result} ({attempt} попытка)")

# Список функций, доступных из модуля
__all__ = ['guess_riddle', 'show_results']
