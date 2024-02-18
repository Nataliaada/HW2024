# Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции
# — функции. Дополнительно сохраняйте все операции поступления и
# снятия средств в список.


def main():
    balance = 0
    count = 0
    operations = []  # создаем пустой список для хранения операций

    print('Добро пожаловать в банкомат!')
    while True:
        while True:
            act = input('Выберите действие:\n 1 - пополнить \n 2 - снять \n 3 - выйти\n 4 - осмотреть список операции\n')
            if act not in ("1", "2", "3","4"):
                print("Неверный ввод")
            else:
                break
        match act:
            case "1":
                balance, count = add_money(balance, count)
                print(f"Ваш баланс {balance}")
                operations.append(('Пополнение', balance))  # добавляем операцию в список
            case "2":
                balance, count = get_money(balance, count)
                print(f"Ваш баланс {balance}")
                operations.append(('Снятие', balance))  # добавляем операцию в список
            case "4":
                print(f"Ваш баланс {balance}")
                print(operations)

            case "3":
                print(f"Ваш баланс {balance}")
                print("До свидания!")
                break

def add_money(balance, count):

    if balance > 5_000_000:
        balance *= 0.9
    while True:
        try:
            summ = int(input("Введите сумму пополнения, кратную 50: "))

        except:
            ex = input("Хотите выйти в меню?\n")
            if ex.lower() == 'да':
                return balance, count
            else:
                continue
        if summ % 50 == 0:
            break
    balance += summ
    count += 1
    if count % 3 == 0:
        balance *= 1.03
    return balance, count

def get_money(balance, count):
    if balance > 5_000_000:
        balance *= 0.9
    while True:
        try:
            summ = int(input("Введите сумму снятия, кратную 50: "))
        except:
            ex = input("Хотите выйти в меню?\n")
            if ex.lower() == 'да':
                return balance, count
            else:
                continue
        if summ % 50 == 0:
            perc = summ * 0.015
            if perc < 30:
                perc = 30
            elif perc > 600:
                perc = 600
            if summ + perc > balance:
                print("Недостаточно средств!")
                continue
            else:
                break
    balance -= (summ + perc)
    count += 1
    if count % 3 == 0:
        balance *= 1.03
    return balance, count
main()
