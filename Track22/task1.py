# Создайте функцию, которая запрашивает числовые данные от
# пользователя до тех пор, пока он не введёт целое или
# вещественное число.
# Обрабатывайте не числовые данные как исключения.

def get_numeric_input():
    while True:
        user_input = input("Введите число: ")
        try:
            numeric_value = float(user_input)  # Попытка преобразовать введенное значение в число
            return numeric_value  # Возврат числового значения, если успешно
        except ValueError:
            print("Ошибка! Введите целое или вещественное число.")

# Пример использования
try:
    number = get_numeric_input()
    print(f"Вы ввели число: {number}")
except KeyboardInterrupt:
    print("\nПрервано пользователем.")
