import sys
import argparse
import os
import shutil
import time
from datetime import datetime, date, timedelta


def create_ar(path):
    if os.path.exists(path + '\Archive') is False:
        os.chdir(path)
        os.mkdir(str('Archive'))


def create_sm(path):
    if os.path.exists(path + '\Small') is False:
        os.chdir(path)
        os.mkdir(str('Small'))


# ------------------------------#Asking console for args
def main():
    m = argparse.ArgumentParser(description="Reorganize", epilog="Mission complete!")
    m.add_argument("--source", type=str, default='.', help='Destination')
    m.add_argument("--days", type=int, default=10, help='How old are files? (days)')
    m.add_argument("--size", type=int, default=4096, help='Max size of files')
    options = m.parse_args()

    # ------------------------------#Convert into str
    options = str(options)
    print(options)
    options = options[9:]
    print(options)
    options = options.replace('(', '')
    options = options.replace(')', '')
    options = options.replace(',', '')
    listOptions = options.split(' ')
    print(listOptions)
    # ------------------------------#Some action here

    # --------------------------#Days param
    daysTo = listOptions[0]
    daysTo = daysTo.split('=')
    daysTo = daysTo[1]
    date_dif = date.today() - timedelta(days=int(daysTo))
    print(daysTo)
    print(date_dif)
    # ----------------------------#Source
    source = listOptions[2]
    source = source.split('=')
    source = source[1]
    print(source)
    source = source.replace('\\\\', '\\')  # \\ na \
    source = source.replace('\'', '')  # ' na del
    print('Source', source)
    # ------------------------------#Size
    size = listOptions[1]
    size = size.split('=')
    size = size[1]
    size = int(size)
    # ----------------------#Is it empty? if not i create folders there and sort files
    if os.path.exists(source) is True:
        if os.listdir(source):
            # Some files
            # Create folders

            files = os.listdir(source)
            files = [os.path.join(source, file) for file in files]
            print(files)
            files = [file for file in files if os.path.isfile(file)]  # files only in list
            print(files)
            for i in range(len(files)):
                print(files[i])
                # Move files
                if date_dif > date.fromtimestamp(os.stat(files[i]).st_mtime):
                    create_ar(source)
                    shutil.move(files[i], source + '\Archive')
                if os.path.exists(files[i]):
                    if os.path.getsize(files[i]) < size:
                        create_sm(source)
                        shutil.move(files[i], source + '\Small')
        else:
            # No any files
            print('Directory is EMPTY!')
            # Nothing to do here ¯\_(ツ)_/¯
            print('YOU SHOULD INPUT CORRECT PATH!')


main()
