while 1:
    print('Введите число:')
    try:
        a = float(input())  # В input'e можно написать сторку для вывода
    except ValueError:
        print('Ввод символов запрещен')
    else:
        if a == 321.0:
            break
        else:
            try:
                if a < 0:
                    raise Warning
            except Warning:
                print('Некорректный формат')
            else:
                b = int((a - int(a)) * 100) # Вычитаем из float int, *100, чтобы взять 2 числа после запятой, преобразуем в int
                print(int(a), "Руб.", b, "Коп.")
