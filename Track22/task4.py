# Вспоминаем задачу из семинара 8 про сериализацию данных,
# где в бесконечном цикле запрашивали имя, личный
# идентификатор и уровень доступа (от 1 до 7) сохраняя
# информацию в JSON файл.
# Напишите класс пользователя, который хранит эти данные в
# свойствах экземпляра.
# Отдельно напишите функцию, которая считывает информацию
# из JSON файла и формирует множество пользователей.

import json

class User:
    def __init__(self, name, id, access_level):
        self.name = name
        self.id = id
        self.access_level = access_level

    def __str__(self):
        return f"Имя: {self.name}, ID: {self.id}, Уровень доступа: {self.access_level}"

def read_users_from_json_file(filename):
    users = set()
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            for user_data in data:
                user = User(user_data['name'], user_data['id'], user_data['access_level'])
                users.add(user)
    except FileNotFoundError:
        print(f"Файл {filename} не найден.")
    except json.JSONDecodeError:
        print(f"Ошибка при чтении данных из файла {filename}.")
    return users

# Пример использования
if __name__ == "__main__":
    # Создаем пользователя и сохраняем в JSON файл
    user1 = User("Alice", 12345, 5)
    user2 = User("Bob", 67890, 3)
    users = {user1, user2}

    with open('users.json', 'w') as file:
        user_data = [{'name': user.name, 'id': user.id, 'access_level': user.access_level} for user in users]
        json.dump(user_data, file)

    # Считываем пользователей из JSON файла
    loaded_users = read_users_from_json_file('users.json')

    # Выводим информацию о загруженных пользователях
    for user in loaded_users:
        print(user)
