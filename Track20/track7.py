# Создайте класс Матрица. Добавьте методы для:
# - вывода на печать,
# - сравнения,
# - сложения,
# - *умножения матриц

class Matrix:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.data = [[0 for _ in range(columns)] for _ in range(rows)]

    def __str__(self):
        matrix_str = ""
        for row in self.data:
            matrix_str += " ".join(map(str, row)) + "\n"
        return matrix_str

    def __eq__(self, other):
        if self.rows != other.rows or self.columns != other.columns:
            return False
        for i in range(self.rows):
            for j in range(self.columns):
                if self.data[i][j] != other.data[i][j]:
                    return False
        return True

    def __add__(self, other):
        if self.rows != other.rows or self.columns != other.columns:
            raise ValueError("Matrix dimensions must match for addition.")
        result = Matrix(self.rows, self.columns)
        for i in range(self.rows):
            for j in range(self.columns):
                result.data[i][j] = self.data[i][j] + other.data[i][j]
        return result

    def __mul__(self, other):
        if self.columns != other.rows:
            raise ValueError("Number of columns in the first matrix must match the number of rows in the second matrix.")
        result = Matrix(self.rows, other.columns)
        for i in range(self.rows):
            for j in range(other.columns):
                for k in range(self.columns):
                    result.data[i][j] += self.data[i][k] * other.data[k][j]
        return result

# Пример использования
matrix1 = Matrix(2, 3)
matrix1.data = [[1, 2, 3], [4, 5, 6]]

matrix2 = Matrix(2, 3)
matrix2.data = [[7, 8, 9], [10, 11, 12]]

matrix3 = matrix1 + matrix2
matrix4 = matrix1 * matrix2

print("Matrix1:")
print(matrix1)

print("Matrix2:")
print(matrix2)

print("Matrix3 (Matrix1 + Matrix2):")
print(matrix3)

print("Matrix4 (Matrix1 * Matrix2):")
print(matrix4)

print("Matrix1 == Matrix2:", matrix1 == matrix2)
