text = str(input('Введите текст: ')).split()
print('Свыше 7 символов:')
for i in range(len(text)):
    if len(text[i]) > 7:
        print(text[i])

print('В промежутке от 4 до 7 символов:')
for i in range(len(text)):
    if 7 >= len(text[i]) >= 4:
        print(text[i])

print('Менее 4 символов:')
for i in range(len(text)):
    if len(text[i]) < 4:
        print(text[i])