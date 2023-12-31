# Доработаем класс Архив из задачи 2.
# Добавьте методы представления экземпляра для программиста
# и для пользователя.

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

    def __str__(self):
        """
        Метод для представления экземпляра класса для пользователя.

        Возвращает:
        str: Строковое представление архива для пользователя.
        """
        return f"Архив с числами: {self.numbers}, строками: {self.strings}"

    def __repr__(self):
        """
        Метод для представления экземпляра класса для программиста.

        Возвращает:
        str: Строковое представление архива для программиста.
        """
        return f"Archive(numbers={self.numbers}, strings={self.strings})"
