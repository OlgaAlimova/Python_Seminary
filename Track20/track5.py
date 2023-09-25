# Дорабатываем класс прямоугольник из прошлого семинара.
# Добавьте возможность сложения и вычитания.
# При этом должен создаваться новый экземпляр
# прямоугольника.
# Складываем и вычитаем периметры, а не длинну и ширину.
# При вычитании не допускайте отрицательных значений.

class Rectangle:
    """
    Класс "Прямоугольник" представляет собой геометрическую фигуру
    с заданными длиной и шириной.

    Атрибуты:
    length (float): Длина прямоугольника.
    width (float): Ширина прямоугольника.
    """

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        """
        Метод для вычисления площади прямоугольника.

        Возвращает:
        float: Площадь прямоугольника.
        """
        return self.length * self.width

    def perimeter(self):
        """
        Метод для вычисления периметра прямоугольника.

        Возвращает:
        float: Периметр прямоугольника.
        """
        return 2 * (self.length + self.width)

    def __add__(self, other):
        """
        Метод для сложения периметров двух прямоугольников.

        Аргументы:
        other (Rectangle): Другой прямоугольник для сложения.

        Возвращает:
        Rectangle: Новый прямоугольник с периметром, равным сумме периметров
                   текущего и другого прямоугольников.
        """
        total_perimeter = self.perimeter() + other.perimeter()
        return Rectangle(total_perimeter / 4, total_perimeter / 4)

    def __sub__(self, other):
        """
        Метод для вычитания периметра другого прямоугольника из текущего.

        Аргументы:
        other (Rectangle): Другой прямоугольник для вычитания.

        Возвращает:
        Rectangle: Новый прямоугольник с периметром, равным разности периметров
                   текущего и другого прямоугольников. Если разность меньше нуля,
                   возвращается прямоугольник с нулевыми сторонами.
        """
        total_perimeter = self.perimeter() - other.perimeter()
        if total_perimeter < 0:
            return Rectangle(0, 0)
        return Rectangle(total_perimeter / 4, total_perimeter / 4)

    def __str__(self):
        return f"Прямоугольник (длина: {self.length}, ширина: {self.width})"

# Пример использования
rectangle1 = Rectangle(4, 5)
rectangle2 = Rectangle(3, 2)

# Сложение периметров
result_add = rectangle1 + rectangle2
print("Сложение периметров:")
print(result_add)

# Вычитание периметров
result_sub = rectangle1 - rectangle2
print("\nВычитание периметров:")
print(result_sub)
