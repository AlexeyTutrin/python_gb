from math import pi


def transform(num: float, value: float) -> float:
    value = str(value)
    value = len(value[value.find('.')+1::])
    return float(f'{pi: 0.{value}f}')


d = input("Введите число для заданной длинны числа Пи: ")
print(f'Число Пи с заданной точностью d равно {transform(pi, d)}')
