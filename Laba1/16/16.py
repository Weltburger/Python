import random

from datetime import datetime, timedelta

TeamList = [
    'Реал Мадрид»',
    'Бавария',
    'Манчестер Юнайтед»',
    'Барселона',
    'Индепендьенте',
    'Бока Хуниорс',
    'Сантос',
    'Ювентус',
    'Пеньяроль',
    'Ривер Плейт',
    'Фламенго',
    'Милан',
    'Ливерпуль',
    'Ботафого',
    'Бенфика',
    'Арсенал'
]

random.shuffle(TeamList)
print('Команды: ')
print('\n'.join(TeamList))

TeamListGroup = [TeamList[i:i + 4] for i in range(0, len(TeamList), 4)]  # range(start, end, step)

print('Жеребьевка')
print('Group A: ', TeamListGroup[0])
print('Group B: ', TeamListGroup[1])
print('Group C: ', TeamListGroup[2])
print('Group D: ', TeamListGroup[3])
print('Расписание матчей')

# -------date----------
tempDate = "14.09.2020"
startTime = [14, 9, 2020]
endTime = [31, 3, 2021]

print('Season starts in', str(startTime[0]) + '/' + str(startTime[1]) + '/' + str(startTime[2]) + ' ' + str('22:45'))
print('Season ends in', str(endTime[0]) + '/' + str(endTime[1]) + '/' + str(endTime[2]) + ' ' + str('22:45'))
now_date = datetime.now()
now_date = now_date.replace(2020, 9, 14)
print('\n')

# ---------------------
a = datetime(2020, 9, 14)
b = timedelta(days=14)
i = 0

print('%s/%s/%s' % (a.day, a.month, a.year) + '   22:45  ' + str(TeamList[i]) + '  &  ' + str(TeamList[i + 1]))
i += 1
a = datetime(2020, 9, 16)

while a <= datetime(2021, 3, 31):  # season end
    a = a + b  # + 14 days
    if (i < 15):
        print('%s/%s/%s' % (a.day, a.month, a.year) + '   22:45  ' + str(TeamList[i]) + '  &  ' + str(TeamList[i + 1]))
        i += 1
    else:
        print('%s/%s/%s' % (a.day, a.month, a.year) + '   22:45  ' + str(TeamList[15]) + '  &  ' + str(TeamList[0]))
        break
