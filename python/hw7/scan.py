def search_contact():
    return input('Введите информацию для поиска контакта: ')


def select_mode():
    return input('Выберите режим(1 - добавить, 2 - поиск): ')


def add_contact():
    contact_name = input('Введите имя контакта: ')
    contact_phone = input('Введите номер контакта: ')
    return f'{contact_name};{contact_phone}'


def search_result(result):
    print('Результат поиска: ')
    for i in result:
        print(i)
