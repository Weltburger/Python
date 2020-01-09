import os
import hashlib

dict = {}
dictDublicates = {}
PATH = "D:/Test"


def getMD5sum(fileName):
    hash = hashlib.md5()
    fd = open(fileName, 'r')
    b = fd.read()
    hash.update(b.encode('utf-8'))
    fd.close()
    return hash.hexdigest()


def paths(path="D:/Test"):
    os.chdir(path)
    for root, dirs, files in os.walk(path, topdown=True):
        for name in files:
            fname = str(os.path.join(root, name))
            md5sum = getMD5sum(fname)
            print(md5sum, 'utf-8')
            if md5sum in dict.keys():
                if md5sum in dictDublicates.keys():
                    dictDublicates[md5sum] += str(fname + ';  ')
                else:
                    dictDublicates[md5sum] = str(fname + ';  ')
            if md5sum in dict.keys():
                dict[md5sum] += str(fname + ';  ')
            else:
                dict[md5sum] = str(fname + ';  ')
            print(os.path.join(root, name))
        for name in dirs:
            print(os.path.join(root, name))


paths("D:/Test")
print('\n')
print('Файлы и их хеш суммы: \n', dict, '\n')
print('Файлы и их хеш суммы, без первого файла(оригинала): \n', dictDublicates)
