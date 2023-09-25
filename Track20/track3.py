# Добавьте к задачам 1 и 2 строки документации для классов.

import time


class MyString(str):
    """
    Класс "Моя Строка" расширяет функциональность стандартного типа str,
    дополнительно хранит информацию о имени автора строки и времени создания.

    Позволяет использовать все стандартные методы и операции для строк.
    Предоставляет доступ к имени автора и времени создания строки с использованием
    специальных методов.

    Атрибуты:
    author (str): Имя автора строки.
    creation_time (float): Время создания строки в формате timestamp.
    """

    def __new__(cls, value, author=None):
        instance = super().__new__(cls, value)
        instance.author = author
        instance.creation_time = time.time()
        return instance


class Archive:
    """
    Класс "Архив" хранит пару свойств, таких как число и строка.
    При создании нового экземпляра класса, данные из ранее созданных
    экземпляров сохраняются в архивных списках. Класс "Архив" также
    предоставляет методы для доступа к архивным данным, включая числа и строки,
    которые были сохранены в предыдущих экземплярах.

    Атрибуты:
    numbers (list): Список чисел, сохраненных в архиве.
    strings (list): Список строк, сохраненных в архиве.
    """

    def __init__(self, number, string):
        self.numbers = []
        self.strings = []
        self.add_data(number, string)

    def add_data(self, number, string):
        """
        Метод для добавления числа и строки в архив.

        Аргументы:
        number (int): Число для добавления в архив.
        string (str): Строка для добавления в архив.
        """
        self.numbers.append(number)
        self.strings.append(string)

    def get_numbers(self):
        """
        Метод для получения списка чисел из архива.

        Возвращает:
        list: Список чисел, сохраненных в архиве.
        """
        return self.numbers

    def get_strings(self):
        """
        Метод для получения списка строк из архива.

        Возвращает:
        list: Список строк, сохраненных в архиве.
        """
        return self.strings