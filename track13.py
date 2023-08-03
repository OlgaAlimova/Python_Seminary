# Создайте функцию генератор чисел Фибоначчи

def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Создаем объект генератора
fib_gen = fibonacci_generator()

# Генерируем первые 10 чисел Фибоначчи и выводим их
for i in range(10):
    print(next(fib_gen))
