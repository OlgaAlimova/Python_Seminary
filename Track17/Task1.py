# Сериализация
# Напишите функцию, которая получает на вход директорию и рекурсивно
# обходит её и все вложенные директории. Результаты обхода сохраните
# в файлы json, csv и pickle.
# Для дочерних объектов указывайте родительскую директорию.
# Для каждого объекта укажите файл это или директория.
# Для файлов сохраните его размер в байтах, а для директорий размер
# файлов в ней с учётом всех вложенных файлов и директорий.
#
# Пример:
# test/users/names.txt
# Результат в json для names.txt:
# {
# "name": names.txt
# "parent": users,
# "type": "file"
# "size": 4096
# }

import os
import json
import csv
import pickle


def get_file_size(file_path):
    try:
        return os.path.getsize(file_path)
    except OSError:
        return 0


def get_directory_size(directory_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(directory_path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            total_size += get_file_size(file_path)
    return total_size


def save_metadata_to_json(directory_path, output_file):
    metadata = []

    for dirpath, dirnames, filenames in os.walk(directory_path):
        for dirname in dirnames:
            dir_info = {
                "name": dirname,
                "parent": os.path.relpath(dirpath, directory_path),
                "type": "directory",
                "size": get_directory_size(os.path.join(dirpath, dirname))
            }
            metadata.append(dir_info)

        for filename in filenames:
            file_info = {
                "name": filename,
                "parent": os.path.relpath(dirpath, directory_path),
                "type": "file",
                "size": get_file_size(os.path.join(dirpath, filename))
            }
            metadata.append(file_info)

    with open(output_file, "w") as json_file:
        json.dump(metadata, json_file, indent=4)


def save_metadata_to_csv(directory_path, output_file):
    fieldnames = ["name", "parent", "type", "size"]
    with open(output_file, "w", newline="") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

        for dirpath, dirnames, filenames in os.walk(directory_path):
            for dirname in dirnames:
                writer.writerow({
                    "name": dirname,
                    "parent": os.path.relpath(dirpath, directory_path),
                    "type": "directory",
                    "size": get_directory_size(os.path.join(dirpath, dirname))
                })

            for filename in filenames:
                writer.writerow({
                    "name": filename,
                    "parent": os.path.relpath(dirpath, directory_path),
                    "type": "file",
                    "size": get_file_size(os.path.join(dirpath, filename))
                })


def save_metadata_to_pickle(directory_path, output_file):
    metadata = []

    for dirpath, dirnames, filenames in os.walk(directory_path):
        for dirname in dirnames:
            dir_info = {
                "name": dirname,
                "parent": os.path.relpath(dirpath, directory_path),
                "type": "directory",
                "size": get_directory_size(os.path.join(dirpath, dirname))
            }
            metadata.append(dir_info)

        for filename in filenames:
            file_info = {
                "name": filename,
                "parent": os.path.relpath(dirpath, directory_path),
                "type": "file",
                "size": get_file_size(os.path.join(dirpath, filename))
            }
            metadata.append(file_info)

    with open(output_file, "wb") as pickle_file:
        pickle.dump(metadata, pickle_file)


# Пример использования
if __name__ == "__main__":
    directory_path = "путь_к_директории"

    # Сохранение метаданных в формате JSON
    save_metadata_to_json(directory_path, "metadata.json")

    # Сохранение метаданных в формате CSV
    save_metadata_to_csv(directory_path, "metadata.csv")

    # Сохранение метаданных в формате pickle
    save_metadata_to_pickle(directory_path, "metadata.pickle")
