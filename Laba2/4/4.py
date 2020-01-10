import re


def find_match(text):
    for i in range(len(text)):
        pattern = re.compile(r'([a-z]{1,}:) (int|short|byte) ([0-9]{1,})')
        result = pattern.findall(text[i])
        searchForResult = pattern.search(text[i])
        if searchForResult is not None:
            print(type(result))
            print('Строка ', i, ', Позиция ', searchForResult.span(), ' найдено : ', result)


def fopen(pathToFile):
    rfile = open(pathToFile)
    fileString = rfile.readlines()
    find_match(fileString)


finish_it = False
while finish_it is not True:
    try:
        _pathToFile = input('Введите путь к файлу: ')
        fopen(_pathToFile)
        finish_it = True
    except(FileNotFoundError, OSError):
        print('Файл не найден!')

# .	Один любой символ, кроме новой строки \n.
# ?	0 или 1 вхождение шаблона слева
# +	1 и более вхождений шаблона слева
# *	0 и более вхождений шаблона слева
# \w	Любая цифра или буква (\W — все, кроме буквы или цифры)
# \d	Любая цифра [0-9] (\D — все, кроме цифры)
# \s	Любой пробельный символ (\S — любой непробельный символ)
# \b	Граница слова
# [..]	Один из символов в скобках ([^..] — любой символ, кроме тех, что в скобках)
# \	Экранирование специальных символов (\. означает точку или \+ — знак «плюс»)
# ^ и $	Начало и конец строки соответственно
# {n,m}	От n до m вхождений ({,m} — от 0 до m)
# a|b	Соответствует a или b
# ()	Группирует выражение и возвращает найденный текст
# \t, \n, \r	Символ табуляции, новой строки и возврата каретки соответственно
