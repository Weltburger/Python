text = str(input('Введите текст: ')).split()
tempText = []
for i in range(len(text)):
    if len(text[i]) > 7:
        tempText.append(text[i])

for i in range(len(text)):
    if 7 >= len(text[i]) >= 4:
        tempText.append(text[i])

for i in range(len(text)):
    if len(text[i]) < 4:
        tempText.append(text[i])

tempText.sort(key=len, reverse=True)
for i in range(len(tempText)):
    print(tempText[i])