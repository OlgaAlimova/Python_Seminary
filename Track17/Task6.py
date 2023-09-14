# Напишите функцию, которая ищет json файлы в указанной
# директории и сохраняет их содержимое в виде
# одноимённых pickle файлов.

import os
import json
import pickle

import Track17


def convert_json_to_pickle(directory):
    # Проверяем, существует ли указанная директория
    if not os.path.exists(directory):
        print(f"Директория '{directory}' не существует.")
        return

    # Ищем JSON-файлы в указанной директории
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            json_filepath = os.path.join(directory, filename)

            # Определяем имя для pickle файла (без расширения)
            pickle_filename = os.path.splitext(filename)[0] + '.pickle'
            pickle_filepath = os.path.join(directory, pickle_filename)

            try:
                # Читаем данные из JSON файла
                with open(json_filepath, 'r') as json_file:
                    data = json.load(json_file)

                # Сохраняем данные в виде pickle файла
                with open(pickle_filepath, 'wb') as pickle_file:
                    pickle.dump(data, pickle_file)

                print(f"Файл '{json_filepath}' успешно конвертирован в '{pickle_filepath}'.")

            except Exception as e:
                print(f"Ошибка при конвертации файла '{json_filepath}': {str(e)}")

if __name__ == "__main__":
    directory_path = Track17  # Заменить на путь к нужной директории
    convert_json_to_pickle(directory_path)
