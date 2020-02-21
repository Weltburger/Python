while 1:
    print('Введите номер карты')
    try:
        arr = [int(el) for el in input().split()]
    except ValueError:
        print('Вводите числа')

    try:
        strCard = str(arr[0]) + str(arr[1]) + str(arr[2]) + str(arr[3])
        for i in arr:
            if not 5 > len(str(i)) > 3:
                raise Warning
    except (Warning, IndexError):
        print('Номер карты введен некорректно')
    except NameError:
        print('Массив не определен')
    else:
        print('Номер карты: ', arr[0], '*' * 12, arr[3])
        print('Номер карты: ', strCard[0:4], '*' * 12, strCard[12:16])
        break
