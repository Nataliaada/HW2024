# Напишите программу, которая получает целое число и возвращает
# его двоичное, восьмеричное строковое представление.
# Функции bin и oct используйте для проверки своего
# результата, а не для решения.
# Дополнительно:
# Попробуйте избежать дублирования кода
# в преобразованиях к разным системам счисления
# Избегайте магических чисел
# Добавьте аннотацию типов где это возможно
#
# def convert_to_base(number: int, base: int) -> str:
#     """
#     Функция для преобразования числа в указанную систему счисления
#
#     Аргументы:
#     number -- число для преобразования
#     base -- основание системы счисления
#
#     Возвращает:
#     Строковое представление числа в указанной системе счисления
#     """
#     # Создание словарей для соответствия чисел и символов
#     digits = "0123456789ABCDEF"
#     value_map = {i: digits[i] for i in range(base)}
#
#     # Обработка особых случаев
#     if number == 0:
#         return "0"
#     elif number < 0:
#         return "-" + convert_to_base(-number, base)
#
#     result = ""
#     while number > 0:
#         number, remainder = divmod(number, base)
#         result = value_map[remainder] + result
#
#     return result
#
#
# def main():
#     number = int(input("Введите целое число: "))
#
#     binary = convert_to_base(number, 2)
#     octal = convert_to_base(number, 8)
#
#     print(f"Двоичное представление числа: {binary}")
#     print(f"Восьмеричное представление числа: {octal}")
#
#
# if __name__ == '__main__':
#     main()
# sql-ex.ru
# pgexercises.com
# sql-academy.org
#


num = int(input('Введите число: '))



result = ''
OCT = 8
BIN = 2
print(bin(num))
while num > 0:
    result = str(num % BIN) + result
    num = num // BIN
print(result)
result = ''
num = int(input('Введите число: '))
print(oct(num))
while num > 0:
    result = str(num % OCT) + result
    num = num // OCT
print(result)


# Напишите программу, которая вычисляет площадь
# круга и длину окружности по введённому диаметру.
# Диаметр не превышает 1000 у.е.
# Точность вычислений должна составлять
# не менее 42 знаков после запятой.

import decimal
import math
decimal.getcontext().prec = 50
PI = decimal.Decimal(math.pi)
d = decimal.Decimal(input('Введите диаметр менее 1000 у.е.: '))
print(f'Площадь круга: {PI * (d/2) ** 2}, длина окружности: {PI * d}')

