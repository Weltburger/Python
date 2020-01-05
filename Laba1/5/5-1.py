text = (str(input('Введите строку: '))).split(' ')

for i in range(len(text)):
    if ((text[i])[0]).isupper():
        text[i] = text[i].upper()
print(' '.join(text))
