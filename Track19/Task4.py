# Создайте класс Сотрудник.
# Воспользуйтесь классом человека из прошлого задания.
# У сотрудника должен быть:
# - шестизначный идентификационный номер
# - уровень доступа вычисляемый как остаток от деления
# суммы цифр id на семь

from Track19.Task3 import Person

class Employee(Person):
    def __init__(self, first_name, last_name, age, employee_id):
        super().__init__(first_name, last_name, age)
        self._employee_id = employee_id

    @property
    def access_level(self):
        # Вычисляем уровень доступа как остаток от деления суммы цифр ID на 7
        id_sum = sum(int(digit) for digit in str(self._employee_id))
        return id_sum % 7

# Пример использования
employee = Employee("Иван", "Иванов", 30, 123456)
print(f"Имя: {employee.full_name()}")
print(f"Возраст: {employee.age} лет")
print(f"ID: {employee.employee_id}")
print(f"Уровень доступа: {employee.access_level}")
