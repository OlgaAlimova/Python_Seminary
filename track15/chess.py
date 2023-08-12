# Известно, что на доске 8×8 можно расставить 8 ферзей так,
# чтобы они не били друг друга. Вам дана расстановка 8 ферзей
# на доске, определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел, каждое число
# от 1 до 8 - координаты 8 ферзей. Если ферзи не бьют друг друга
# верните истину, а если бьют - ложь.
# Напишите функцию в шахматный модуль. Используйте генератор
# случайных чисел для случайной расстановки ферзей в задаче выше.
# Проверяйте различный случайные  варианты и выведите 4 успешных расстановки.

import random


def is_safe(board):
    for i in range(8):
        for j in range(i + 1, 8):
            if board[i] == board[j] or abs(board[i] - board[j]) == j - i:
                return False
    return True


def generate_random_board():
    return [random.randint(1, 8) for _ in range(8)]


def find_safe_board():
    attempts = 0
    while attempts < 1000:
        board = generate_random_board()
        if is_safe(board):
            return board
        attempts += 1
    return None


def print_board(board):
    for row in board:
        print(" ".join("Q" if col == row else "." for col in range(1, 9)))


if __name__ == "__main__":
    successful_boards = []

    for _ in range(4):
        safe_board = find_safe_board()
        if safe_board:
            successful_boards.append(safe_board)

    for i, board in enumerate(successful_boards):
        print(f"Successful Board {i + 1}:")
        print_board(board)
        print()

__all__ = ['is_safe', 'generate_random_board', 'find_safe_board', 'print_board']