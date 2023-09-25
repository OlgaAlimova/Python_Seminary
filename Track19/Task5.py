# Создайте три (или более) отдельных классов животных.
# Например рыбы, птицы и т.п.
# У каждого класса должны быть как общие свойства,
# например имя, так и специфичные для класса.
# Для каждого класса создайте метод, выводящий
# информацию специфичную для данного класса.

class Animal:
    def __init__(self, name):
        self.name = name

class Fish(Animal):
    def __init__(self, name, water_type):
        super().__init__(name)
        self.water_type = water_type

    def info(self):
        print(f"Рыба по имени {self.name} живет в воде типа {self.water_type}")

class Bird(Animal):
    def __init__(self, name, wingspan):
        super().__init__(name)
        self.wingspan = wingspan

    def info(self):
        print(f"Птица по имени {self.name} имеет размах крыльев {self.wingspan} см")

class Mammal(Animal):
    def __init__(self, name, fur_color):
        super().__init__(name)
        self.fur_color = fur_color

    def info(self):
        print(f"Млекопитающее по имени {self.name} имеет цвет шерсти {self.fur_color}")

# Пример использования
fish = Fish("Немо", "соленая")
bird = Bird("Сокол", 90)
mammal = Mammal("Лев", "желтый")

fish.info()  # Выводит информацию о рыбе
bird.info()  # Выводит информацию о птице
mammal.info()  # Выводит информацию о млекопитающем

