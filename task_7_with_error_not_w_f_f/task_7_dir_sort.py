from os import listdir, path, mkdir, replace
from pathlib import Path

__all__ = ['sort_files']

DICT_EXT = {'Music': ('mp3', 'wav', 'acc', 'flac'),
            'Videos': ('mp4', 'avi', 'mpeg'),
            'Imagine': ('jpeg', 'png', 'raw', 'tiff', 'gif'),
            'Text': ('txt', 'doc', 'bin')}


def sort_files(directory):
    file_list = [files for files in listdir(directory)]
    for file in file_list:
        if path.isfile(directory + '/' + file):
            for fold, exts in DICT_EXT.items():
                if file.split('.')[-1] in exts:
                    dir_file = check_dir(directory, fold)
                    replace(directory + '/' + file, (dir_file + '/' + file))
    return file_list


def check_dir(dir_file, folder):
    fold_name = dir_file + folder
    if not folder in listdir(dir_file):
        mkdir(fold_name)
    return fold_name


if __name__ == "__main__":
    sort_files("C://Users//OneDrive//Рабочий стол//Py_task7")
