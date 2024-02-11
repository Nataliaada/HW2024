# Создайте несколько переменных разных типов.
# Проверьте к какому типу относятся созданные переменные.

a: int = 5
b: str = 'Hello world!'
c: float = 3.14159
d: list = [8, 6]
e: dict = {'a': 1, 'b': 2, 'c': 4}
f: set = {7, 'end', 56}
g: tuple = (5, 7, 8)

print(type(a), type(b), type(c))

# Создайте в переменной data список значений разных типов перечислив их через запятую внутри квадратных скобок. Для каждого элемента в цикле выведите:
# порядковый номер начиная с единицы
# значение
# адрес в памяти
# размер в памяти
# хэш объекта
# результат проверки на целое число только если он положительный
# результат проверки на строку только если он положительный
# Добавьте в список повторяющиеся элементы и сравните на результаты.
data = [a, b, c, d, e, a, f, d, g]
for i, j in enumerate(data):
    print(i + 1, j, id(data[i]), sys.getsizeof(data[i]),
          hash(data[i]) if type(data[i]) in [int, float, str, tuple] else '',
          'Целое число' if isinstance(data[i], int) else '',
          'Строка' if type(data[i]) == str else '')