#  Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
#  Программа должна подсказывать “больше” или “меньше” после каждой попытки.
#  Для генерации случайного числа используйте код:
# from random import randintnum = randint(LOWER_LIMIT, UPPER_LIMIT)
from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
MAX_ATTEMPTS = 10

# Загадываем число
secret_num = randint(LOWER_LIMIT, UPPER_LIMIT)

# Запускаем цикл угадывания
for attempt in range(MAX_ATTEMPTS):
    # Пользователь вводит предполагаемое число
    guess = int(input("Попытка № {}: Введите число от {} до {}: ".format(attempt + 1, LOWER_LIMIT, UPPER_LIMIT)))

    # Проверяем, больше или меньше загаданное число
    if guess < secret_num:
        print("Загаданное число больше")
    elif guess > secret_num:
        print("Загаданное число меньше")
    else:
        print("Поздравляю! Вы угадали число!")
        break

# Если все попытки исчерпаны, выводим ответ
if attempt == MAX_ATTEMPTS - 1:
    print("Вы не смогли угадать число. Загаданное число было:", secret_num)
