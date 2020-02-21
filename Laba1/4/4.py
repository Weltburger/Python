text = str(input('Введите текст: ')).split()
tempText = [i for i in text if len(i) > 7]

for i in text:
    if 7 >= len(i) >= 4:
        tempText.append(i)

for i in text:
    if len(i) < 4:
        tempText.append(i)

tempText.sort(key=len, reverse=True)
for i in tempText:
    print(i)