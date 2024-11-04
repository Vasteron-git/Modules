import os
import time

# текущая директория
directory = "."
# обход каталога
for root, dirs, files in os.walk(directory):
    for file in files:
        # полный путь к файлу
        filepath = os.path.join(root, file)
        # время изменения файла
        filetime = os.path.getmtime(filepath)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        # размер файла
        filesize = os.path.getsize(filepath)
        # род.дир. файла
        parent_dir = os.path.dirname(filepath)
        # инфа о файле
        print(            f'Обнаружен файл: {file},'
                          f' Путь: {filepath}, Размер: {filesize} байт, Время изменения:'
                          f' {formatted_time}, Родительская директория: {parent_dir}')
