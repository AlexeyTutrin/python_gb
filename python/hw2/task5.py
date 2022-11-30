from random import randint

array = list(map(int, input().split()))
print(f'Первоначальный список: {array}')
for i in range(len(array)-1):
    n = randint(0, len(array)-1)
    array[i], array[n] = array[n], array[i]
print(f'Перемешанный списко: {array}')
