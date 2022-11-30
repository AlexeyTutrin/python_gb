a = int(input('Введите число: '))
result = [(1+1/i)**i for i in range(1, a+1)]
print(f'Cписок из n чисел последовательности: {result}')
print(f'Сумма из последовательности n чисел : {sum(result)}')
