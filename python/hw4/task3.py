array = list(map(int, input("Введите числа через пробел:\n").split()))
print(f"Исходный массив: {array}")
new_array = []
[new_array.append(i) for i in array if i not in new_array]
print(f"Массив из неповторяющихся элементов: {new_array}")
