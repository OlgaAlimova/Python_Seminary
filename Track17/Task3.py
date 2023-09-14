# Напишите функцию, которая в бесконечном цикле
# запрашивает имя, личный идентификатор и уровень
# доступа (от 1 до 7).
# После каждого ввода добавляйте новую информацию в
# JSON файл.
# Пользователи группируются по уровню доступа.
# Идентификатор пользователя выступает ключём для имени.
# Убедитесь, что все идентификаторы уникальны независимо
# от уровня доступа.
# При перезапуске функции уже записанные в файл данные
# должны сохраняться.


import json

def add_user_to_json():
    try:
        with open('users.json', 'r') as file:
            users_data = json.load(file)
    except FileNotFoundError:
        users_data = {}

    while True:
        name = input("Введите имя пользователя (или 'q' для завершения): ")
        if name == 'q':
            break

        user_id = input("Введите личный идентификатор пользователя: ")
        access_level = input("Введите уровень доступа (от 1 до 7): ")
        access_level = int(access_level)

        # Убедимся, что идентификатор пользователя уникален
        if user_id in users_data:
            print("Пользователь с таким идентификатором уже существует. Попробуйте еще раз.")
            continue

        # Создаем словарь с данными пользователя
        user_info = {
            "name": name,
            "id": user_id,
            "access_level": access_level
        }

        # Группируем пользователей по уровню доступа
        if access_level not in users_data:
            users_data[access_level] = {}

        users_data[access_level][user_id] = user_info

        # Сохраняем данные в JSON-файл
        with open('users.json', 'w') as file:
            json.dump(users_data, file, indent=4)

        print("Пользователь успешно добавлен.")

if __name__ == "__main__":
    add_user_to_json()
