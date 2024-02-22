# Напишите функцию, которая принимает на вход строку - абсолютный путь
# до файла. Функция возвращает кортеж из трёх элементов: путь, имя файла,
# расширение файла.



# filename = file_path[file_path.rfind('/') + 1:]
# print(filename)
# corteg1=()



def parse_file_path(file_path):
    return file_path.rpartition('/')[0], \
           file_path.rpartition('/')[-1].rsplit('.', 1)[0], \
           file_path.rpartition('/')[-1].rsplit('.', 1)[1]

link = "/path/to/file.txt"
print(parse_file_path(link))