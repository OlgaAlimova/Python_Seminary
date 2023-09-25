# Создайте класс окружность.
# Класс должен принимать радиус окружности при создании
# экземпляра.
# У класса должно быть два метода, возвращающие длину
# окружности и её площадь.


import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def circumference(self):
        """
        Метод для вычисления длины окружности.
        """
        return 2 * math.pi * self.radius

    def area(self):
        """
        Метод для вычисления площади круга.
        """
        return math.pi * self.radius ** 2

# Создаем экземпляр класса Circle с радиусом 5
circle = Circle(5)

# Вычисляем длину окружности
circumference = circle.circumference()
print(f"Длина окружности: {circumference:.2f}")

# Вычисляем площадь круга
area = circle.area()
print(f"Площадь круга: {area:.2f}")
