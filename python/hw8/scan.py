def search_employee():
    return input('Введите информацию для поиска контакта: ')


def select_mode():
    return input('Выберите режим(1-добавить,2-поиск,3-изменить,4-удалить): ')


def add_employee():
    employee_name = input('Введите имя работника: ')
    employee_phone = input('Введите номер работника: ')
    employee_position = input('Введите должность работника: ')
    return f'{employee_name}||{employee_phone}||{employee_position}'


def search_result(result):
    print('Результат поиска: ')
    for i in result:
        print(i)


def clarification():
    return input('Введите id: ')


def error():
    print('Введено некорректное значение')
