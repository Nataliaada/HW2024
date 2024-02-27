# Напишите функцию в шахматный модуль. Используйте
# генератор случайных чисел для случайной расстановки ферзей в задаче выше.
# Проверяйте  различный случайные варианты
# и выведите 4 успешных расстановки.
from random import randint
from HW6_1 import are_queens_safe

import random

def generate_random_queens():
    queens_positions = []
    unique_positions = set()
    while len(unique_positions) < 8:
        x = random.randint(1, 8)
        y = random.randint(1, 8)
        position = (x, y)
        if position not in unique_positions:
            queens_positions.append(position)
            unique_positions.add(position)
    return queens_positions

print(generate_random_queens())

successful_arrangements = 0
attempts = 0

while successful_arrangements < 4:
    attempts+=1
    queens_positions = generate_random_queens()
    result = are_queens_safe(queens_positions)
    print(queens_positions)
    print(result)
    if not result:
        successful_arrangements += 1
        print(f"Успешная расстановка ферзей {successful_arrangements}: {queens_positions}")
print(f"Всего попыток: {attempts}")
