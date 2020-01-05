text = str(input('Введите текст: ')).split()
for i in range(len(text)):
    if text[i].istitle():   # Можно (text[i])[0].isupper() | istitle проверяет для каждого слова в строке
        print(text[i].upper(), end=' ')
    else:
        print(text[i], end=' ')

