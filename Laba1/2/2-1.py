from sys import stdin, exit as sys_exit
isGrowing = True

print("Введите массив чисел")
try:
    arr = [int(el) for el in input().split()]

except ValueError:
    print('Вводите числа')
    sys_exit()

try:
    for i in range(0, len(arr) - 1):
        if arr[i] > arr[i + 1]:
            isGrowing = False
            break

except IndexError:
    print('Массив слишком мал или пуст')
    sys_exit()
except NameError:
    print('Массив arr не определен')
    sys_exit()
else:
    if len(arr) - 2 >= 0:
        if isGrowing is True:
            print('True')
        else:
            print('False')