# 2. Дан список повторяющихся элементов. Вернуть список с дублирующимися
# элементами. В результирующем списке не должно быть дубликатов.
#
# def get_duplicates_without_duplicates(lst):
#     duplicates = []  # Список для хранения дублирующихся элементов
#     seen = set()  # Множество для отслеживания уже встреченных элементов
#
#     for item in lst:
#         if item not in seen:  # Если элемент еще не встречался
#             seen.add(item)  # Добавляем его во множество "seen"
#         else:
#             duplicates.append(item)  # Если элемент уже встречался, добавляем его в список "duplicates"
#
#     return list(set(duplicates))  # Возвращаем список с уникальными дубликатами
#

my_list = [1, 2, 3, 2, 4, 4, 5, 3]
duplicates =[]
n_list=set()
for item in my_list:
    if item not in n_list:  # Если элемент еще не встречался
        n_list.add(item)  # Добавляем его во множество "n_list"
    else:
        duplicates.append(item)
print(list(set(duplicates)))