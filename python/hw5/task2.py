import random


def show_field():
    global field

    print("\n")
    print("\t     |     |")
    print(f"\t  {field[0]}  |  {field[1]}  |  {field[2]}")
    print("\t_____|_____|_____")

    print("\t     |     |")
    print(f"\t  {field[3]}  |  {field[4]}  |  {field[5]}")
    print("\t_____|_____|_____")

    print("\t     |     |")
    print(f"\t  {field[6]}  |  {field[7]}  |  {field[8]}")
    print("\t     |     |")
    print("\n")


def ChoosePos():
    global tie
    global field
    while True:
        positions = int(input('Введите позицию от 1 до 9: '))
        if type(field[positions-1]) != "":
            field[positions-1] = 'X'
            tie += 1
            break
        else:
            print('Данная позиция занята')


def ChooseBot():
    global field
    global tie
    while True:
        positions = random.randint(0, 8)
        if type(field[positions]) == int:
            print(f'Бот выбрал {positions+1} клетку')
            field[positions] = 'O'
            tie += 1
            break


def Winner(field):
    win = False
    combs = [[0, 1, 2],
             [3, 4, 5],
             [6, 7, 8],
             [0, 4, 8],
             [0, 3, 6],
             [1, 4, 7],
             [2, 4, 6],
             [2, 5, 8]]
    for pos in combs:
        if field[pos[0]] == field[pos[1]] == field[pos[2]]:
            win = True
    return win


field = [1, 2, 3, 4, 5, 6, 7, 8, 9]
tie = 0
players = ['Человек', 'Бот']
choice = random.choice(players)
print(f'Первым ходит {choice}')
show_field()

while True:
    if choice == 'Игрок1':
        show_field()
        ChoosePos()
        choice = 'Бот'
        if Winner(field):
            print('Победил Игрок1')
            break
        elif tie == 9:
            print('Ничья')
            break
    else:
        show_field()
        ChooseBot()
        choice = 'Игрок1'
        if Winner(field):
            print('Победил Бот')
            break
        elif tie == 9:
            print('Ничья')
            break
