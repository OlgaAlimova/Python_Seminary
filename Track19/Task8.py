# Возьмите 1-3 любые задания из прошлых семинаров
# (например сериализация данных), которые вы уже решали.
# Превратите функции в методы класса, а параметры в свойства.
# Задания должны решаться через вызов методов экземпляра.

# исходная задача

import json

def save_data_to_json(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file)

def load_data_from_json(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

# после преобразования

import json

class JSONDataHandler:
    def __init__(self, filename):
        self.filename = filename

    def save_data(self, data):
        with open(self.filename, 'w') as file:
            json.dump(data, file)

    def load_data(self):
        with open(self.filename, 'r') as file:
            data = json.load(file)
        return data

# Пример использования
data_handler = JSONDataHandler('data.json')
data_to_save = {'name': 'John', 'age': 30, 'city': 'New York'}
data_handler.save_data(data_to_save)

loaded_data = data_handler.load_data()
print(loaded_data)
