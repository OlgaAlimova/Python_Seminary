# Напишите программу, которая получает целое число и возвращает
# его шестнадцатеричное строковое представление. Функцию hex
# используйте для проверки своего результата.

def int_to_hex_string(number):
    hex_string = hex(number)[2:]  # Используем срез [2:], чтобы удалить префикс "0x"
    return hex_string.upper()  # Преобразуем результат в верхний регистр

# Пример использования
try:
    number = int(input("Введите целое число: "))
    hex_string = int_to_hex_string(number)
    print("Шестнадцатеричное представление числа:", hex_string)
    print("Проверка с помощью hex():", hex_string == hex(number)[2:].upper())
except ValueError:
    print("Ошибка: Введите целое число.")

