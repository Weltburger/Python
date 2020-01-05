text = str(input('Введите текст: ')).split()
arr = [i for i in text]  # Генератор списков
print(arr)
for i in range(len(arr)):
    if arr[i].startswith('www.'):
        arr[i] = 'http://' + arr[i]
    if not arr[i].endswith('.com'):
        arr[i] += '.com'
print(arr)
