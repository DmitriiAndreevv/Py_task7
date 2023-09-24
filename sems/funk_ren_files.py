# 3. Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами.
import os
from sem_1 import my_func
from sem_2 import my_func as my_func2
from sem_4 import create_files_with_extension
from sem_5 import create_dif_files
from sem_6 import group

if __name__ == '__main__':
    my_func(10, 'file_1.txt')
    my_func2(10, 'file_2.txt')  # функцию, которая генерирует псевдоимена.
    create_files_with_extension('bin')  # функция, которая создаёт файлы с указанным расширением.
    create_dif_files(txt=2, bin=4, png=8)  # функцию которая генерирует файлы с разными расширениями
    group(os.getcwd())  # функция для сортировки файлов по директориям: видео, изображения, текст и т.п
