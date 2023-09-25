# Доработайте прошлую задачу.
# Добавьте сравнение прямоугольников по площади
# Должны работать все шесть операций сравнения

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

    def __eq__(self, other):
        """
        Метод для сравнения прямоугольников на равенство по площади.

        Аргументы:
        other (Rectangle): Другой прямоугольник для сравнения.

        Возвращает:
        bool: True, если площади прямоугольников равны, иначе False.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Метод для сравнения прямоугольников на неравенство по площади.

        Аргументы:
        other (Rectangle): Другой прямоугольник для сравнения.

        Возвращает:
        bool: True, если площади прямоугольников не равны, иначе False.
        """
        return self.area() != other.area()

    def __lt__(self, other):
        """
        Метод для сравнения прямоугольников по площади: меньше.

        Аргументы:
        other (Rectangle): Другой прямоугольник для сравнения.

        Возвращает:
        bool: True, если площадь текущего прямоугольника меньше площади
              другого прямоугольника, иначе False.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Метод для сравнения прямоугольников по площади: меньше или равно.

        Аргументы:
        other (Rectangle): Другой прямоугольник для сравнения.

        Возвращает:
        bool: True, если площадь текущего прямоугольника меньше или равна площади
              другого прямоугольника, иначе False.
        """
        return self.area() <= other.area()

    def __gt__(self, other):
        """
        Метод для сравнения прямоугольников по площади: больше.

        Аргументы:
        other (Rectangle): Другой прямоугольник для сравнения.

        Возвращает:
        bool: True, если площадь текущего прямоугольника больше площади
              другого прямоугольника, иначе False.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Метод для сравнения прямоугольников по площади: больше или равно.

        Аргументы:
        other (Rectangle): Другой прямоугольник для сравнения.

        Возвращает:
        bool: True, если площадь текущего прямоугольника больше или равна площади
              другого прямоугольника, иначе False.
        """
        return self.area() >= other.area()

    def __str__(self):
        return f"Прямоугольник (длина: {self.length}, ширина: {self.width})"

# Пример использования
rectangle1 = Rectangle(4, 5)
rectangle2 = Rectangle(3, 6)

# Сравнение площадей
print("Сравнение площадей:")
print(rectangle1 == rectangle2)  # Площади равны
print(rectangle1 != rectangle2)  # Площади не равны
print(rectangle1 < rectangle2)   # Площадь rectangle1 меньше
print(rectangle1 <= rectangle2)  # Площадь rectangle1 меньше или равна
print(rectangle1 > rectangle2)   # Площадь rectangle2 больше
print(rectangle1 >= rectangle2)  # Площадь rectangle2 больше или равна
