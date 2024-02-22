 # Создайте функцию генератор чисел Фибоначчи

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Создаем генератор чисел Фибоначчи
fib = fibonacci()

# Выводим первые 10 чисел Фибоначчи
for i, num in enumerate(fibonacci(), start=1):
    print(num)
    if i == 10:
        break
