# Возьмите 1-3 задачи из тех, что были на прошлых
# семинарах или в домашних заданиях. Напишите к ним
# классы исключения с выводом подробной информации.
# Поднимайте исключения внутри основного кода. Например
# нельзя создавать прямоугольник со сторонами
# отрицательной длины.

class InvalidRectangleError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class Rectangle:
    def __init__(self, length, width):
        if length <= 0 or width <= 0:
            raise InvalidRectangleError("Прямоугольник должен иметь положительные стороны.")
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

# Пример использования
try:
    rectangle = Rectangle(-5, 10)
except InvalidRectangleError as e:
    print(f"Ошибка: {e.message}")
else:
    print(f"Площадь прямоугольника: {rectangle.area()}")
    print(f"Периметр прямоугольника: {rectangle.perimeter()}")

