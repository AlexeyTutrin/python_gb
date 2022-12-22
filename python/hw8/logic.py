import csv


def employee_add(employee, id):
    employee = f'{id} || ' + employee
    try:
        with open('book.txt', 'a', encoding='utf-8') as book:
            book.write(f'\n{employee}')
    except FileNotFoundError:
        with open('book.txt', 'w', encoding='utf-8') as book:
            book.write(f'{employee}')
    log_csv(employee, id)


def take_warp():
    with open('book.txt', 'r', encoding='utf-8') as book:
        return book.read()


def log_csv(employee, id):
    employee = f'{id} || ' + employee
    employee = [employee.split(' || ')]
    try:
        with open('book.csv', 'a', encoding='utf-8') as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerows(employee)
    except FileNotFoundError:
        with open('book.csv', 'w', encoding='utf-8') as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerows(employee)


def update_warp(new_info):
    new_info_file = [i.split(' || ') for i in new_info]
    with open('book.csv', 'a', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter=';')
        for row in new_info_file:
            writer.writerow(row)
    with open('book.txt', 'a', encoding='utf-8') as book:
        book.write('\n'.join(new_info))
