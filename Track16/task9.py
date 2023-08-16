# Генерация файлов с разными расширениями

import os
import random
import string


def generate_random_filename(length):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))


def generate_files_with_extensions(extensions, min_name_length=6, max_name_length=30, min_bytes=256, max_bytes=4096,
                                   num_files=42):
    for extension in extensions:
        directory = f"generated_files/{extension}"
        if not os.path.exists(directory):
            os.makedirs(directory)

        for _ in range(num_files):
            filename = generate_random_filename(random.randint(min_name_length, max_name_length))
            file_path = os.path.join(directory, f"{filename}.{extension}")
            with open(file_path, "wb") as f:
                num_bytes = random.randint(min_bytes, max_bytes)
                f.write(os.urandom(num_bytes))

__all__ = ["generate_files_with_extensions"]

# Пример использования
if __name__ == "__main__":
    extensions = ['txt', 'pdf', 'jpg', 'png', 'mp4', 'docx']
    generate_files_with_extensions(extensions)
    print("Файлы успешно сгенерированы с разными расширениями.")
