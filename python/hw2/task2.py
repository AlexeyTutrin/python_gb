import math

a = int(input('Введите целое число: '))
result = [math.factorial(i) for i in range(1, a+1)]
print(f'Набор произведений чисел от 1 до N равно: {result}')
