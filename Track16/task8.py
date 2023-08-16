# Групповое переименование файлов

import os

def rename_files_with_counter(directory, extension, new_name, num_digits, final_extension=None, char_range=None):
    for index, file in enumerate(os.listdir(directory)):
        if file.endswith('.' + extension):
            current_name, ext = os.path.splitext(file)
            if char_range:
                current_name = current_name[char_range[0]:char_range[1]]
            new_file_name = f"{new_name}_{str(index).zfill(num_digits)}"
            if final_extension:
                new_file_name += '.' + final_extension
            new_file_path = os.path.join(directory, new_file_name)
            old_file_path = os.path.join(directory, file)
            os.rename(old_file_path, new_file_path)

__all__ = ["rename_files_with_counter"]

# Пример использования
if __name__ == "__main__":
    target_directory = "sorted_files/images"
    extension = "jpg"
    new_name = "image"
    num_digits = 3
    final_extension = "jpeg"
    rename_files_with_counter(target_directory, extension, new_name, num_digits, final_extension, char_range=(2, 5))
    print("Файлы успешно переименованы с использованием счётчика.")
