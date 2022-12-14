from random import randint
k = int(input('Введите натуральную степень k: '))

factor = [randint(0, 100) for i in range(k)]+[randint(1, 100)]
polinom = '+'.join([f'{(j,"")[j==1]}x^{i}' for i,
                   j in enumerate(factor) if j][::-1])
print(f'Список коэффициентов {factor}')
polinom = polinom.replace('x^1+', 'x+')
polinom = polinom.replace('x^0', '')
with open('Task04.txt', 'w') as data:
    data.write(polinom)
