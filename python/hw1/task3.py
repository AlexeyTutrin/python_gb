x = int(input())
y = int(input())

if x > 0 and y > 0:
    print('1-ая четверть')
elif x < 0 and y > 0:
    print('2-ая четверть')
elif x < 0 and y < 0:
    print('3-ая четверть')
elif x > 0 and y < 0:
    print('4-ая четверть')
elif x == 0 and y == 0:
    print('Центр')
elif x == 0:
    print('на оси Y')
elif y == 0:
    print('на оси X')
