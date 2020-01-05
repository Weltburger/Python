import re
from sys import stdin, exit as sys_exit

password = input('Введите пароль: ')
mark = 0
if password == '' or len(password) < 4:
    print('Пароль не соответствует начальным требованиям')
    sys_exit()
else:
    if 4 < len(password):
        mark += 15
    if len(password) >= 16:
        mark += 15
    if re.search(r'[A-Z]', password):
        mark += 30
    if re.search(r'[a-z]', password):
        mark += 10
    if re.search(r'[0-9]', password):
        mark += 30

print('Ваш пароль набрал: {} баллов'.format(mark))
