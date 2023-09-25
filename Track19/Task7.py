# Доработаем задания 5-6. Создайте класс-фабрику.
# - Класс принимает тип животного (название одного из созданных классов)
# и параметры для этого типа.
# - Внутри класса создайте экземпляр на основе переданного типа и
# верните его из класса-фабрики.

class Animal:
    def __init__(self, name):
        self.name = name

    def info(self):
        pass

class Fish(Animal):
    def __init__(self, name, water_type):
        super().__init__(name)
        self.water_type = water_type

    def info(self):
        print(f"Рыба: {self.name}, Тип воды: {self.water_type}")

class Bird(Animal):
    def __init__(self, name, wingspan):
        super().__init__(name)
        self.wingspan = wingspan

    def info(self):
        print(f"Птица: {self.name}, Размах крыльев: {self.wingspan} см")

class Mammal(Animal):
    def __init__(self, name, fur_color):
        super().__init__(name)
        self.fur_color = fur_color

    def info(self):
        print(f"Млекопитающее: {self.name}, Цвет меха: {self.fur_color}")

class AnimalFactory:
    @staticmethod
    def create_animal(animal_type, **kwargs):
        if animal_type == "Fish":
            return Fish(**kwargs)
        elif animal_type == "Bird":
            return Bird(**kwargs)
        elif animal_type == "Mammal":
            return Mammal(**kwargs)
        else:
            raise ValueError(f"Тип животного '{animal_type}' не найден")

# Пример использования
fish = AnimalFactory.create_animal("Fish", name="Немо", water_type="соленая")
bird = AnimalFactory.create_animal("Bird", name="Сокол", wingspan=90)
mammal = AnimalFactory.create_animal("Mammal", name="Лев", fur_color="желтый")

fish.info()  # Выводит информацию о рыбе
bird.info()  # Выводит информацию о птице
mammal.info()  # Выводит информацию о млекопитающем
