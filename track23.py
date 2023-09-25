# Возьмите 1-3 задания из тех, что были на прошлых семинарах или в домашних заданиях. Напишите к ним тесты.
# 2-5 тестов на задание в трёх вариантах:
# - doctest,
# - unittest,
# - pytest.

# Задача: Напишите функцию, которая находит среднее арифметическое чисел в списке.

def calculate_average(numbers):
    """
    Функция принимает список чисел и возвращает их среднее арифметическое.

    >>> calculate_average([1, 2, 3, 4, 5])
    3.0

    >>> calculate_average([10, 20, 30, 40, 50])
    30.0

    >>> calculate_average([2, 4, 6, 8, 10])
    6.0
    """
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

# 1. Тесты с использованием doctest:

import doctest

doctest.testmod()

# 2. Тесты с использованием unittest:

import unittest

class TestCalculateAverage(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(calculate_average([1, 2, 3, 4, 5]), 3.0)

    def test_large_numbers(self):
        self.assertEqual(calculate_average([10, 20, 30, 40, 50]), 30.0)

    def test_even_numbers(self):
        self.assertEqual(calculate_average([2, 4, 6, 8, 10]), 6.0)

    def test_empty_list(self):
        self.assertEqual(calculate_average([]), 0)

if __name__ == '__main__':
    unittest.main()

# 3. Тесты с использованием pytest:

import pytest

def test_positive_numbers():
    assert calculate_average([1, 2, 3, 4, 5]) == 3.0

def test_large_numbers():
    assert calculate_average([10, 20, 30, 40, 50]) == 30.0

def test_even_numbers():
    assert calculate_average([2, 4, 6, 8, 10]) == 6.0

def test_empty_list():
    assert calculate_average([]) == 0
