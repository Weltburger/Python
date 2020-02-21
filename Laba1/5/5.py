text = str(input('Введите текст: ')).split()
for i in text:
    if i.istitle():   # Можно (text[i])[0].isupper() | istitle проверяет для каждого слова в строке
        print(i.upper(), end=' ')
    else:
        print(i, end=' ')

