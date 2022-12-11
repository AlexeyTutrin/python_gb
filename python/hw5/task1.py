import random

candy = int(input('Введите кол-во конфет больше 28: '))


def ChooseCandyQuantity():
    global candy
    while True:
        choice = int(input('Введите кол-во конфет от 1 до 28: '))
        if choice > 0 and choice < 29 and choice <= candy:
            candy -= choice
            break
        else:
            print('Такое кол-во конфет нельзя')


def BotChoose():
    global candy
    choice = random.randint(1, 28)
    print(f'Бот взял {choice} конфет')
    candy -= choice


print(f'На столе лежит {candy} конфет')
players = ['Человек', 'Бот']
choice = random.choice(players)
print(f'Первым ходит {choice}')

while True:
    if choice == 'Игрок1':
        ChooseCandyQuantity()
        print(f'Кол-во конфет: {candy}')
        choice = 'Бот'
        if candy < 29:
            print(f'Победил {choice}')
            break
    else:
        BotChoose()
        print(f'Кол-во конфет: {candy}')
        choice = 'Игрок1'
        if candy < 29:
            print(f'Победил {choice}')
            break
