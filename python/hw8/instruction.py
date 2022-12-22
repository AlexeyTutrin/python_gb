import logic
import pattern
import scan


def change():
    employee = scan.search_employee()
    warp = logic.take_warp()
    result = pattern.employee_search(warp, employee)
    scan.search_result(result)
    if 'не найден' not in result[0] and len(warp.split('\n')) > 1:
        result = pattern.employee_search(warp, scan.clarification())[0]
        new_employee = scan.add_employee()
        update = pattern.employee_edit(warp, result, new_employee)
        logic.update_warp(update)
    elif 'не найден' not in result[0]:
        result = warp.split('\n')[0]
        new_employee = scan.add_employee()
        update = pattern.employee_edit(warp, result, new_employee)
        logic.update_warp(update)


def start():
    while True:
        mode = scan.select_mode()
        if mode == '1':
            employee = scan.add_employee()
            warp = logic.take_warp()
            id = pattern.create_id(warp)
            logic.employee_add(employee, id)
        elif mode == '2':
            employee = scan.search_employee()
            warp = logic.take_warp()
            result = pattern.employee_search(warp, employee)
            scan.search_result(result)
        elif mode == '3':
            change()
        elif mode == '4':
            employee = scan.search_employee()
            warp = logic.take_warp()
            result = pattern.employee_search(warp, employee)
            scan.search_result(result)
            if 'не найден' not in result[0] and len(warp.split('\n')) > 1:
                result = pattern.employee_search(warp, scan.clarification())[0]
                update = pattern.employee_delete(warp, result)
                logic.update_warp(update)
            elif 'не найден' not in result[0]:
                result = warp.split('\n')[0]
                update = pattern.employee_delete(warp, result)
                logic.update_warp(update)
        else:
            scan.error()
