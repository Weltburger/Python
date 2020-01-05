start_sum = input('Введите необходимую сумму: ')
fertig = True
count_0 = len(list(start_sum)) - 1
partition_sum = int(start_sum)
bank = dict([(1000, 10), (500, 10), (100, 10), (50, 10), (10, 10)])
bank_copy = bank.copy()
bills = list(bank.keys())
j = 0
for i in range(len(list(start_sum))):
    divider = int('1' + count_0 * '0')
    remain = partition_sum % divider
    partition_sum = partition_sum - remain
    while partition_sum > 0:
        if bank[bills[j]] == 0 or partition_sum - bills[j] < 0:
            if bank[bills[4]] == 0 or partition_sum - bills[4] < 0:
                fertig = False
                print('Невозможно произвести операцию! Нехватает купюр')
                bank = bank_copy
                partition_sum = 0
                break
            j += 1
        else:
            partition_sum = partition_sum - bills[j]
            bank[bills[j]] -= 1
    partition_sum = remain
    count_0 -= 1
if fertig:
    differ = []
    for i in range(len(bank)):
        differ = bank_copy[bills[i]] - bank[bills[i]]
        if i == len(bank) - 1:
            print(differ, '*', bills[i], sep=' ')
        else:
            print(differ, '*', bills[i], sep=' ', end=' + ')
print(bank)
