# Напишите функцию принимающую на вход только ключевые параметры
# и возвращающую словарь, где ключ — значение переданного аргумента,
# а значение — имя аргумента. Если ключ не хешируем, используйте его
# строковое представление.

def create_argument_dict(**kwargs):
    argument_dict = {}
    for key, value in kwargs.items():
        key_str = str(key) if hashable(key) else repr(key)
        argument_dict[key_str] = value.__name__ if hasattr(value, '__name__') else type(value).__name__
    return argument_dict

def hashable(obj):
    try:
        hash(obj)
        return True
    except TypeError:
        return False

# Пример использования функции
def example_function(a, b, c='default', d=None):
    argument_dict = create_argument_dict(a=a, b=b, c=c, d=d)
    print(argument_dict)

example_function(10, 'hello', c=42, d=lambda x: x ** 2)
