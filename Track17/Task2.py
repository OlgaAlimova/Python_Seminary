# Напишите функцию, которая создаёт из созданного ранее
# файла новый с данными в формате JSON.
# Имена пишите с большой буквы.
# Каждую пару сохраняйте с новой строки.

import json

import Track16
from Track16 import task1
from Track16 import task2
from Track16 import task3


def multiply_and_save_as_json(numbers_file, names_file, output_file):
    with open(numbers_file, 'r') as num_file, open(names_file, 'r') as name_file:
        numbers_lines = num_file.readlines()
        names_lines = name_file.readlines()

    # Проверяем, сколько строк в каждом файле
    min_length = min(len(numbers_lines), len(names_lines))

    result_data = []

    for i in range(min_length):
        number = float(numbers_lines[i].strip().split('|')[1])  # Берем второе число из строки файла с числами
        name = names_lines[i].strip().capitalize()  # Преобразуем имя к формату с заглавной буквой

        # Перемножаем числа и готовим данные для сохранения в формате JSON
        result = {'name': name, 'result': round(abs(number * 1.0), 0)}
        if number < 0:
            result['name'] = name.lower()

        result_data.append(result)

    # Сохраняем результаты в JSON файл
    with open(output_file, 'w') as json_file:
        json.dump(result_data, json_file, indent=4)


# Пример использования:
numbers_file = Track16/task1
names_file = Track16/task2
output_json_file = Track16/task3
multiply_and_save_as_json(numbers_file, names_file, output_json_file)
