# Добавьте в пакет, созданный на семинаре шахматный модуль.
# Внутри него напишите код, решающий задачу о 8 ферзях. Известно, что на доске
# 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
# Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара
# бьющих друг друга. Программа получает на вход восемь пар чисел, каждое число
# от 1 до 8 - координаты 8 ферзей. Если ферзи не бьют друг друга верните истину,
# а если бьют - ложь.


def are_queens_safe(queens):
    for i in range(len(queens)):
        for j in range(i+1, len(queens)):
            x1, y1 = queens[i]
            x2, y2 = queens[j]
            if x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2):
                return False
    return True

queens_positions = [(1, 7), (2, 4), (3, 2), (4, 8), (5, 6), (6, 1), (7, 3), (8, 5)]

result = are_queens_safe(queens_positions)
if result:
    print("Ферзи не бьют друг друга.")
else:
    print("Ферзи бьют друг друга.")
