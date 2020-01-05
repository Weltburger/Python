import random

count = random.randint(1, 20)
print('Количество элементов в списке {}'.format(count))


def numbers_range(a):
    for i in range(a):
        yield random.randint(1, 100)


arr = list(numbers_range(count))
cz = 2
while cz < count:
    for j in range(10000):
        if cz >= count:
            print('2 в степени {0} = {1}'.format(j - 1, cz))
            break
        else:
            cz = 2 ** j
difference = cz - count
print('Необходимо добавить {} нулей'.format(difference))
for k in range(difference):
    arr.append(0)
print(arr)
