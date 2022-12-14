number = input('Введите вещественное число: ')

new_sum = sum(map(int, str(number).replace('.', '')))
print(f"Сумма цифр в этом числе = {new_sum}")
