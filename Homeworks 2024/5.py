# 3. Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем
# и знаменателем. Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions
#

from fractions import Fraction

fraction_str = input("Введите первую дробь (в формате a/b): ")
fraction_str_2 = input("Введите вторую дробь (в формате a/b): ")

# # Преобразование строки в объект Fraction

# # Примеры вычислений с дробью
sum_fraction = Fraction(fraction_str) + Fraction(fraction_str_2)
product_fraction = Fraction(fraction_str) * Fraction(fraction_str_2)

print("Исходная дробь 1:", Fraction(fraction_str))
print("Исходная дробь 2:", Fraction(fraction_str_2))
print("Сумма дробей:", sum_fraction)
print("Произведение дробей:", product_fraction)
