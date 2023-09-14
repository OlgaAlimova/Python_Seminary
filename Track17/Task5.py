# Прочитайте созданный в прошлом задании csv файл без
# использования csv.DictReader.
# Дополните id до 10 цифр незначащими нулями.
# В именах первую букву сделайте прописной.
# Добавьте поле хеш на основе имени и идентификатора.
# Получившиеся записи сохраните в json файл, где каждая строка
# csv файла представлена как отдельный json словарь.
# Имя исходного и конечного файлов передавайте как аргументы
# функции.

import csv
import json

def process_csv_to_json(input_csv_filename, output_json_filename):
    processed_data = []

    # Открываем CSV-файл для чтения
    with open(input_csv_filename, 'r', newline='') as csvfile:
        csv_reader = csv.reader(csvfile)

        # Прочитаем заголовок
        header = next(csv_reader)

        for row in csv_reader:
            name = row[0].capitalize()
            id = row[1].zfill(10)
            access_level = int(row[2])

            name_id_hash = hash(f"{name}_{id}")

            user_info = {
                header[0]: name,
                header[1]: id,
                header[2]: access_level,
                'hash': name_id_hash
            }

            processed_data.append(user_info)

    # Сохраняем обработанные данные в JSON-файл
    with open(output_json_filename, 'w') as jsonfile:
        json.dump(processed_data, jsonfile, indent=4)

if __name__ == "__main__":
    input_csv_filename = 'users.csv'
    output_json_filename = 'processed_users.json'

    process_csv_to_json(input_csv_filename, output_json_filename)
    print(f"Данные обработаны и сохранены в файл '{output_json_filename}'.")
