import os
import time

directory = os.getcwd()

for root, dirs, files in os.walk(directory):
    if len(files) != 0:
        for file in files:
            file_abs_path = os.path.join(root, file)
            file_size = os.path.getsize(file_abs_path)
            file_parent_dir = os.path.dirname(file_abs_path)
            file_mod_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(os.path.getmtime(file_abs_path)))
            print("Обнаружен файл:\n",
                  f"\tИмя: {file}\n",
                  f"\tПуть: {file_abs_path}\n",
                  f"\tРазмер: {file_size} байт\n",
                  f"\tВремя последнего изменения: {file_mod_time}\n",
                  f"\tРодительская директория: {file_parent_dir}\n")