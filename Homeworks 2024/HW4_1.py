# Напишите функцию для транспонирования матрицы

def transpond_matrix(matr):
    transpond_matrixs = []
    for j in range(len(matr[0])):
        new_row = []
        for i in range(len(matr)):
            new_row.append(matr[i][j])
        transpond_matrixs.append(new_row)
    return transpond_matrixs


# Пример использования
matr1 = [[1, 2, 3, 4],
         [5, 6, 7, 8 ],
         [9,10,11,12]]

tr = transpond_matrix(matr1)
for row in tr:
    print(row)
