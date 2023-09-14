# Напишите функцию, которая сохраняет созданный в
# прошлом задании файл в формате CSV.

import json
import csv

def save_json_to_csv():
    try:
        with open('users.json', 'r') as file:
            users_data = json.load(file)
    except FileNotFoundError:
        print("Файл 'users.json' не найден.")
        return

    # Открываем CSV-файл для записи
    with open('users.csv', 'w', newline='') as csvfile:
        fieldnames = ['name', 'id', 'access_level']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Записываем заголовок
        writer.writeheader()

        # Записываем данные пользователей
        for access_level, users in users_data.items():
            for user_id, user_info in users.items():
                writer.writerow(user_info)

    print("Данные сохранены в файл 'users.csv' в формате CSV.")

if __name__ == "__main__":
    save_json_to_csv()
