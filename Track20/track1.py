# Создайте класс Моя Строка, где:
# будут доступны все возможности str
# дополнительно хранятся имя автора строки и время создания
# (time.time)

import time

class MyString(str):
    def __init__(self, value, author):
        super().__init__(value)
        self.author = author
        self.creation_time = time.time()

    def __str__(self):
        return super().__str__()

# Пример использования
my_string = MyString("Hello, World!", "John")
print(my_string)  # Выводит: Hello, World!
print(my_string.author)  # Выводит: John
print(my_string.creation_time)  # Выводит время создания строки
