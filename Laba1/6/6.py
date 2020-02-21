text = list(input('Введите текст: '))   # Можно использовать .lower() для приведения к нижнему регистру
for i in text:
    if text.count(i) == 1:
        print(i, end='\n')