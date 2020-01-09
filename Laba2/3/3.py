import os
import re

path = "H:/0Универ\Python\Laba2/3\Music"
# print(path)
basepath = os.path.abspath(os.path.dirname('Music'))  # Возвращает абсол. нормализ. путь (имя директории пути (path))
path = os.path.join(basepath, 'Music')  # Соединяет пути с учётом особенностей операционной системы
# ----------------------------------------------

songList = open('H:/0Универ\Python\Laba2/3\Music\Music.txt', 'r')
formatedList = songList.readlines()  # Считывает из файла все строки в список и возвращает его
dict = {}

for line in range(len(formatedList)):
    arr = formatedList[line]
    arr = arr.split(' ')
    name = formatedList[line]
    name = re.sub('\n', ' ', name)  # Заменяет pos1 на pos2 в pos3 (ошибка \n в конце строки)
    print('temp2  ' + name)
    dict[arr[1] + '.mp3'] = str(name)

for root, dirs, files in os.walk(path, topdown=True):
    for nm in files:
        fname = os.path.join(root, nm)
        fname = str(fname)  # .encode('utf-8')
        print(fname)
        print(' nm ' + nm)
        print('DICT.KEYS  ', dict.keys())
        if nm in dict.keys():
            os.rename(fname, root + "\\" + dict[nm] + '.mp3')
