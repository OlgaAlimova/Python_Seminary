# Сортировка файлов по директориям

import os
import shutil


def sort_files_by_category(source_directory, target_directory):
    categories = {
        'video': ['.mp4', '.avi', '.mkv'],
        'images': ['.jpg', '.png', '.gif'],
        'documents': ['.txt', '.pdf', '.docx'],
    }

    if not os.path.exists(target_directory):
        os.mkdir(target_directory)

    for category, extensions in categories.items():
        category_dir = os.path.join(target_directory, category)
        if not os.path.exists(category_dir):
            os.mkdir(category_dir)

        for root, dirs, files in os.walk(source_directory):
            for file in files:
                for ext in extensions:
                    if file.endswith(ext):
                        src_file_path = os.path.join(root, file)
                        dest_file_path = os.path.join(category_dir, file)
                        shutil.move(src_file_path, dest_file_path)

__all__ = ["sort_files_by_category"]

# Пример использования
if __name__ == "__main__":
    source_directory = "generated_files"
    target_directory = "sorted_files"
    sort_files_by_category(source_directory, target_directory)
    print("Файлы успешно отсортированы по директориям.")
