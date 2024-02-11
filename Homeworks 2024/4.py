# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое
# представление. Функцию hex используйте для проверки своего результата.
#
#
number = 133
hex_string = hex(number)
print(hex_string)

num = int(input('Введите число: '))
HEX = 16
hex_dict = {
    10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F',
}
result = ''
while num > 0:
    remainder = num % HEX
    if remainder > 9:
        result = hex_dict[remainder] + result
    else:
        result = str(remainder) + result
    num = num // HEX
print(result)
