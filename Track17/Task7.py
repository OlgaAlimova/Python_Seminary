# Напишите функцию, которая преобразует pickle файл
# хранящий список словарей в табличный csv файл.
# Для тестированию возьмите pickle версию файла из задачи
# 4 этого семинара.
# Функция должна извлекать ключи словаря для заголовков
# столбца из переданного файла.

import pickle
import csv

def pickle_to_csv(pickle_file, csv_file):
    try:
        # Открываем файл в формате pickle для чтения
        with open(pickle_file, 'rb') as f:
            data = pickle.load(f)

        # Определяем заголовки столбцов на основе ключей первого словаря
        if data:
            fieldnames = data[0].keys()
        else:
            print("Файл pickle пуст.")
            return

        # Записываем данные в файл CSV
        with open(csv_file, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)

        print(f"Данные из '{pickle_file}' успешно записаны в '{csv_file}' в формате CSV.")

    except FileNotFoundError:
        print(f"Файл '{pickle_file}' не найден.")
    except Exception as e:
        print(f"Ошибка: {str(e)}")

if __name__ == "__main__":
    pickle_file_path = 'data.pickle'  # Заменить на путь к файлу pickle
    csv_file_path = 'data.csv'  # Здесь будет сохранен файл CSV
    pickle_to_csv(pickle_file_path, csv_file_path)
