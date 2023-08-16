# Генерация файлов в указанной директории

import os
import random
import string

def generate_files_in_directory(directory, num_files):
    for _ in range(num_files):
        filename = ''.join(random.choice(string.ascii_letters) for _ in range(10))
        file_path = os.path.join(directory, filename)
        with open(file_path, "wb") as f:
            num_bytes = random.randint(256, 4096)
            f.write(os.urandom(num_bytes))

__all__ = ["generate_files_in_directory"]

# Пример использования
if __name__ == "__main__":
    target_directory = "custom_directory"
    if not os.path.exists(target_directory):
        os.makedirs(target_directory)
    generate_files_in_directory(target_directory, 10)
    print("Файлы успешно сгенерированы в указанной директории.")
