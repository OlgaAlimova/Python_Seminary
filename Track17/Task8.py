# Прочитайте созданный в прошлом задании csv файл без
# использования csv.DictReader.
# Распечатайте его как pickle строку.

import csv


def read_csv_to_pickle_string(csv_file):
    try:
        data = []
        with open(csv_file, mode='r', newline='') as file:
            csv_reader = csv.reader(file)
            headers = next(csv_reader)  # Считываем заголовки
            for row in csv_reader:
                data.append(dict(zip(headers, row)))  # Создаем словарь из строки и заголовков
        return data

    except FileNotFoundError:
        print(f"Файл '{csv_file}' не найден.")
        return None
    except Exception as e:
        print(f"Ошибка: {str(e)}")
        return None


if __name__ == "__main__":
    csv_file_path = 'data.csv'  # Заменить на путь к файлу CSV
    csv_data = read_csv_to_pickle_string(csv_file_path)

    if csv_data:
        pickle_string = pickle.dumps(csv_data)
        print(pickle_string)
