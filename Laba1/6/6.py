text = list(input('Введите текст: '))   # Можно использовать .lower() для приведения к нижнему регистру
for i in range(len(text)):
    if text.count(text[i]) == 1:
        print(text[i], end='\n')