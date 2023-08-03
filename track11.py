# Напишите функцию, которая принимает на вход строку — абсолютный
# путь до файла. Функция возвращает кортеж из трёх элементов:
# путь, имя файла, расширение файла.

import os

def split_file_path(file_path):
    file_dir, file_name = os.path.split(file_path)
    file_name, file_extension = os.path.splitext(file_name)
    return file_dir, file_name, file_extension

if __name__ == "__main__":
    file_path = input("Введите абсолютный путь до файла: ")
    path, name, extension = split_file_path(file_path)
    print("Путь:", path)
    print("Имя файла:", name)
    print("Расширение файла:", extension)
