# Напишите следующие функции:
#
# Нахождение корней квадратного уравнения
# Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
# Декоратор, запускающий функцию нахождения корней квадратного уравнения
# с каждой тройкой чисел из csv файла.
# Декоратор, сохраняющий переданные параметры и результаты работы функции
# в json файл.

import math
import csv
import random
import json

# Нахождение корней квадратного уравнения:
def find_quadratic_roots(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return root1, root2
    elif discriminant == 0:
        root1 = -b / (2 * a)
        return root1
    else:
        return "No real roots"

# Генерация CSV файла:
def generate_csv_file(file_name, num_rows):
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        for _ in range(num_rows):
            row = [random.randint(1, 1000) for _ in range(3)]
            writer.writerow(row)

# Декоратор для нахождения корней квадратного уравнения:
def quadratic_roots_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, tuple):
            with open('results.json', 'a') as file:
                data = {
                    "parameters": args,
                    "roots": result
                }
                json.dump(data, file)
            return result
        else:
            return result
    return wrapper

# Декоратор для сохранения параметров и результатов в JSON:
def save_to_json_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        with open('results.json', 'a') as file:
            data = {
                "function": func.__name__,
                "parameters": args,
                "result": result
            }
            json.dump(data, file)
        return result
    return wrapper

# Применяем декораторы к функции нахождения корней квадратного уравнения
@quadratic_roots_decorator
@save_to_json_decorator
def find_quadratic_roots(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return root1, root2
    elif discriminant == 0:
        root1 = -b / (2 * a)
        return root1
    else:
        return "No real roots"

# Генерируем CSV файл
generate_csv_file('random_numbers.csv', 100)

# Считываем CSV файл и применяем функцию к каждой строке
with open('random_numbers.csv', newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        a, b, c = map(int, row)
        find_quadratic_roots(a, b, c)
