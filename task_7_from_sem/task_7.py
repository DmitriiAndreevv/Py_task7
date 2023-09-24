# Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
#  Каждая группа включает файлы с несколькими расширениями.
# В исходной папке должны остаться только те файлы, которые не подошли для сортировки.

import os
from pathlib import Path


def file_replace() -> None:
    global DICTONARY

    for key in DICTONARY.keys():
        if key not in os.listdir():
            os.mkdir(key)

    for key, value in DICTONARY.items():
        for file in os.listdir():
            if os.path.isfile(file) and file.split(".")[-1] in value:
                os.replace(file, os.path.join(os.getcwd(), key, file))


if __name__ == "__main__":
    DICTONARY = {'Music': ('mp3', 'wav', 'acc', 'flac'),
                 'Videos': ('mp4', 'avi', 'mpeg'),
                 'Imagine': ('jpeg', 'png', 'raw', 'tiff', 'gif'),
                 'Text': ('txt', 'doc', 'bin')}

    file_replace()
