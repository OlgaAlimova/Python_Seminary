# Генерация файлов с разными расширениями

import random
from task4 import create_files_with_extension

def generate_files_with_multiple_extensions(extensions, num_files_per_extension):
    for extension in extensions:
        create_files_with_extension(extension, num_files=num_files_per_extension)

__all__ = ["generate_files_with_multiple_extensions"]

# Пример использования
if __name__ == "__main__":
    extensions = ['txt', 'csv', 'log', 'xml', 'json']
    num_files_per_extension = 5
    generate_files_with_multiple_extensions(extensions, num_files_per_extension)
    print(f"Сгенерировано файлов с разными расширениями: {', '.join(extensions)}")
