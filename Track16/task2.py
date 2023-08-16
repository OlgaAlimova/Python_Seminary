# Генерация псевдоимен

import random
import string

def generate_pseudo_names(file_name, num_names):
    vowels = 'aeiou'
    names = []
    with open(file_name, 'a') as file:
        for _ in range(num_names):
            name_length = random.randint(4, 7)
            name = random.choice(string.ascii_uppercase) + ''.join(random.choice(string.ascii_lowercase) for _ in range(name_length - 1))
            name = name[:random.randint(1, name_length)] + random.choice(vowels) + name[name_length:]
            names.append(name)
            file.write(name + '\n')
    return names

__all__ = ["generate_pseudo_names"]

# Пример использования
if __name__ == "__main__":
    file_name = "pseudo_names.txt"
    num_names = 10
    generated_names = generate_pseudo_names(file_name, num_names)
    print(f"Сгенерировано {num_names} псевдоимен и сохранено в файл '{file_name}'.")

