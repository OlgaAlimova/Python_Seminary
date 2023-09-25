# Напишите класс для хранения информации о человеке:
# ФИО, возраст и т.п. на ваш выбор.
# У класса должны быть методы birthday для увеличения
# возраста на год, full_name для вывода полного ФИО и т.п. на
# ваш выбор.
# Убедитесь, что свойство возраст недоступно для прямого
# изменения, но есть возможность получить текущий возраст.

class Person:
    def __init__(self, first_name, last_name, age):
        self._first_name = first_name
        self._last_name = last_name
        self._age = age

    @property
    def age(self):
        return self._age

    def birthday(self):
        self._age += 1

    def full_name(self):
        return f"{self._first_name} {self._last_name}"

# Пример использования
person = Person("Иван", "Иванов", 30)
print(f"Имя: {person.full_name()}")
print(f"Возраст: {person.age} лет")

# Празднуем день рождения
person.birthday()
print(f"После дня рождения: {person.age} лет")
