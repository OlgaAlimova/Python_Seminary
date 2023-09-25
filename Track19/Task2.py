# Создайте класс прямоугольник.
# Класс должен принимать длину и ширину при создании
# экземпляра.
# У класса должно быть два метода, возвращающие периметр
# и площадь.
# Если при создании экземпляра передаётся только одна
# сторона, считаем что у нас квадрат.


class Rectangle:
    def __init__(self, length, width=None):
        self.length = length
        self.width = width if width is not None else length

    def perimeter(self):
        """
        Метод для вычисления периметра прямоугольника.
        """
        return 2 * (self.length + self.width)

    def area(self):
        """
        Метод для вычисления площади прямоугольника.
        """
        return self.length * self.width

# Прямоугольник с длиной 5 и шириной 3
rectangle1 = Rectangle(5, 3)
print(f"Периметр: {rectangle1.perimeter()}")
print(f"Площадь: {rectangle1.area()}")

# Квадрат с длиной 4 (ширина автоматически установится как 4)
square = Rectangle(4)
print(f"Периметр квадрата: {square.perimeter()}")
print(f"Площадь квадрата: {square.area()}")
