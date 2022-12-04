a = int(input('Введите целое число: '))
result = ""

while a != 0:
    result = str(a % 2) + result
    a //= 2
print(result)
