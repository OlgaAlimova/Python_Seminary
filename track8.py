# Напишите функцию для транспонирования матрицы.

def transpose_matrix(matrix):
    # Получаем количество строк и столбцов в исходной матрице
    rows = len(matrix)
    cols = len(matrix[0])

    # Создаем новую матрицу с размерами cols x rows
    transposed_matrix = [[0 for _ in range(rows)] for _ in range(cols)]

    # Заполняем новую матрицу значениями из исходной матрицы
    for i in range(rows):
        for j in range(cols):
            transposed_matrix[j][i] = matrix[i][j]

    return transposed_matrix

def main():
    matrix = [
        [1, 2, 3],
        [4, 5, 6]
    ]

    print("Исходная матрица:")
    for row in matrix:
        print(row)

    transposed_matrix = transpose_matrix(matrix)

    print("\nТранспонированная матрица:")
    for row in transposed_matrix:
        print(row)

if __name__ == "__main__":
    main()
