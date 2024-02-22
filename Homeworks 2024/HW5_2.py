# Напишите однострочный генератор словаря, который принимает на вход
# три списка одинаковой длины: имена str, ставка int, премия str
# с указанием процентов вида “10.25%”. В результате получаем словарь
# с именем в качестве ключа и суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии



def calc_bonus(names: list, salary: list, bonus: list) -> dict:
    return {name: sal * float(bon.strip('%')) / 100 for name, sal, bon in zip(names, salary, bonus)}


if __name__ == '__main__':
    list1 = ['vasily', 'petr', 'maria']
    list2 = [100, 130, 375]
    list3 = ['5.1%', '10.45%', '7.54%']
    print(*zip(list1, list2, list3))
    print(calc_bonus(list1, list2, list3))