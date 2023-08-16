# Создание файлов с указанным расширением

import os
import random
import string

def generate_file_name():
    length = random.randint(6, 30)
    name = ''.join(random.choice(string.ascii_lowercase) for _ in range(length))
    return name

def create_files_with_extension(extension, min_length=256, max_length=4096, num_files=42):
    for _ in range(num_files):
        file_name = generate_file_name() + '.' + extension
        file_size = random.randint(min_length, max_length)
        with open(file_name, 'wb') as file:
            file.write(os.urandom(file_size))

__all__ = ["create_files_with_extension"]

# Пример использования
if __name__ == "__main__":
    extension = "dat"
    create_files_with_extension(extension)
    print(f"Создано {num_files} файлов с расширением '{extension}'.")
