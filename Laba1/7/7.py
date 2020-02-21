# text = str(input('Введите текст: ')).split()
# arr = [i for i in text]  # Генератор списков
# print(arr)
# for i in range(len(arr)):
#     if arr[i].startswith('www.'):
#         arr[i] = 'http://' + arr[i]
#     if not arr[i].endswith('.com'):
#         arr[i] += '.com'
# print(arr)


def check(txt):
    if txt.startswith('www.'):
        txt = 'http://' + txt
    if not txt.endswith('.com'):
        txt += '.com'
    return txt


text = str(input('Введите текст: ')).split()

arr = [check(x) for x in text]
print(arr)
