# Доработайте классы исключения так, чтобы они выдали
# подробную информацию об ошибках.
# Передавайте необходимые данные из основного кода
# проекта.

import json

class User:
    def __init__(self, name, id, access_level):
        self.name = name
        self.id = id
        self.access_level = access_level

    def __str__(self):
        return f"Имя: {self.name}, ID: {self.id}, Уровень доступа: {self.access_level}"

    def __eq__(self, other):
        if isinstance(other, User):
            return self.id == other.id
        return False

class Project:
    def __init__(self, users_filename):
        self.users = self.read_users_from_json_file(users_filename)

    def read_users_from_json_file(self, filename):
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

    def enter_system(self, name, id):
        user_to_find = User(name, id, 0)
        if user_to_find not in self.users:
            raise UserNotFoundError(name, id)
        else:
            for user in self.users:
                if user == user_to_find:
                    return user.access_level

    def add_user(self, name, id, access_level):
        new_user = User(name, id, access_level)
        if new_user.access_level < self.enter_system(name, id):
            raise AccessError(name, id, new_user.access_level)
        else:
            self.users.add(new_user)

class AccessError(Exception):
    def __init__(self, name, id, required_access_level):
        self.name = name
        self.id = id
        self.required_access_level = required_access_level
        self.message = f"Недостаточно прав для доступа. Пользователь: {name}, ID: {id}, Требуемый уровень доступа: {required_access_level}"
        super().__init__(self.message)

class UserNotFoundError(Exception):
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.message = f"Пользователь не найден. Пользователь: {name}, ID: {id}"
        super().__init__(self.message)

# Пример использования
if __name__ == "__main__":
    # Создаем экземпляр класса Project, загружаем пользователей
    project = Project('users.json')

    # Вход в систему
    try:
        user_access_level = project.enter_system("Alice", 12345)
        print(f"Уровень доступа пользователя: {user_access_level}")
    except AccessError as e:
        print(e)

    # Добавление пользователя
    try:
        project.add_user("Eve", 54321, 2)
        print("Пользователь добавлен.")
    except AccessError as e:
        print(e)

