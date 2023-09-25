# Создайте функцию аналог get для словаря.
# Помимо самого словаря функция принимает ключ и
# значение по умолчанию.
# При обращении к несуществующему ключу функция должна
# возвращать дефолтное значение.
# Реализуйте работу через обработку исключений.

def get_from_dict(dictionary, key, default_value=None):
    try:
        return dictionary[key]
    except KeyError:
        return default_value

# Пример использования
my_dict = {'a': 1, 'b': 2, 'c': 3}
result = get_from_dict(my_dict, 'b', default_value=0)
print(result)  # Выведет: 2

result = get_from_dict(my_dict, 'x', default_value=0)
print(result)  # Выведет: 0, так как ключ 'x' отсутствует
