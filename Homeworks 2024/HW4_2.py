# 2. Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.

def create_dict(**kwargs):
    result = {}
    for key, value in kwargs.items():
        if hashable(value):
            result[value] = key
        else:
            result[str(value)] = key
    return result

def hashable(value):
    try:
        hash(value)
        return True
    except TypeError:
        return False

# Пример использования функции
args_dict = create_dict(a=10, b='hello', c=[1, 2, 3], d={'key': 'value'})

print(args_dict)
