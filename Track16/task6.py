# Генерация файлов в указанную директорию

import os
from task4 import create_files_with_extension


def generate_files_in_directory(directory, extensions, num_files_per_extension):
    if not os.path.exists(directory):
        os.mkdir(directory)

    for extension in extensions:
        create_files_with_extension(extension, num_files=num_files_per_extension)

__all__ = ["generate_files_in_directory"]

# Пример использования
if __name__ == "__main__":
    target_directory = "generated_files"
    extensions = ['txt', 'csv', 'log']
    num_files_per_extension = 3
    generate_files_in_directory(target_directory, extensions, num_files_per_extension)
    print(f"Сгенерировано файлов в директории '{target_directory}' с расширениями: {', '.join(extensions)}")
