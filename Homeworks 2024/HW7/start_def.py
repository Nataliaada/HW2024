from filess_pack import HW7_1 as hf
if __name__ == '__main__':
    print("Переименование txt файлов в каталоге data_files")
    files_cnt = hf.group_rename_files("_fn_", ".txt", path="./data_files")
    print(f"Переименовано: {files_cnt}")
