# Создайте класс Архив, который хранит пару свойств.
# Например, число и строку.
# При нового экземпляра класса, старые данные из ранее
# созданных экземпляров сохраняются в пару списковархивов
# list-архивы также являются свойствами экземпляра

class Archive:
    def __init__(self, number, string):
        self.numbers_archive = []
        self.strings_archive = []
        self.add_to_archive(number, string)

    def add_to_archive(self, number, string):
        self.numbers_archive.append(number)
        self.strings_archive.append(string)

    def get_numbers_archive(self):
        return self.numbers_archive

    def get_strings_archive(self):
        return self.strings_archive

# Пример использования
archive1 = Archive(42, "Hello")
archive2 = Archive(99, "World")
archive3 = Archive(123, "Python")

# Получение архивных данных
numbers_archive = archive3.get_numbers_archive()
strings_archive = archive3.get_strings_archive()

print(numbers_archive)  # Выводит: [42, 99, 123]
print(strings_archive)  # Выводит: ['Hello', 'World', 'Python']
