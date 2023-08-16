# Заполнение файла случайными парами чисел

import random

def fill_file_with_random_numbers(file_name, num_lines):
    with open(file_name, 'a') as file:
        for _ in range(num_lines):
            int_number = random.randint(-1000, 1000)
            float_number = random.uniform(-1000, 1000)
            line = f"{int_number}|{float_number:.2f}\n"
            file.write(line)

__all__ = ["fill_file_with_random_numbers"]

# Пример использования
if __name__ == "__main__":
    file_name = "random_numbers.txt"
    num_lines = 10
    fill_file_with_random_numbers(file_name, num_lines)
    print(f"Файл '{file_name}' заполнен случайными парами чисел.")

