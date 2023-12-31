# Напишите код, который запрашивает число и сообщает является ли оно
# простым или составным. Используйте правило для проверки: “Число
# является простым, если делится нацело только на единицу и на себя”.
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

try:
    num = int(input("Введите число (от 2 до 100000): "))
    if num < 2 or num > 100000:
        print("Ошибка: Введите число от 2 до 100000.")
    elif is_prime(num):
        print(f"{num} является простым числом.")
    else:
        print(f"{num} является составным числом.")
except ValueError:
    print("Ошибка: Введите целое число.")
