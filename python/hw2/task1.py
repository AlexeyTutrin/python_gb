a = input('Введите вещественное число: ')
result = 0
for i in a:
    if i != '.':
        result += int(i)
print(f'Сумма цифр в этом числе равна: {result}')
