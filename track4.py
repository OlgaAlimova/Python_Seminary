# Напишите программу, которая принимает две строки вида “a/b” - дробь
# с числителем и знаменателем. Программа должна возвращать сумму и
# произведение* дробей. Для проверки своего кода используйте модуль fractions.

from fractions import Fraction

def add_fractions(fraction1, fraction2):
    return fraction1 + fraction2

def multiply_fractions(fraction1, fraction2):
    return fraction1 * fraction2

def main():
    try:
        fraction_str1 = input("Введите первую дробь в формате 'a/b': ")
        fraction_str2 = input("Введите вторую дробь в формате 'a/b': ")

        numerator1, denominator1 = map(int, fraction_str1.split('/'))
        numerator2, denominator2 = map(int, fraction_str2.split('/'))

        fraction1 = Fraction(numerator1, denominator1)
        fraction2 = Fraction(numerator2, denominator2)

        sum_result = add_fractions(fraction1, fraction2)
        product_result = multiply_fractions(fraction1, fraction2)

        print("Сумма дробей:", sum_result)
        print("Произведение дробей:", product_result)

    except ValueError:
        print("Ошибка: Введите две дроби в правильном формате 'a/b'.")

if __name__ == "__main__":
    main()

