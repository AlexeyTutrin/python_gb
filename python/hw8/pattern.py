def create_id(warp):
    if len(warp.split('\n')) == 0:
        return 1
    else:
        return int(warp.split('\n')[len(warp.split('\n'))-1].split(' || ')[0])+1


def employee_search(warp: str, employee: str) -> list[str]:
    warp = warp.split('\n')
    flag = True
    results = []
    for i in warp:
        if employee in i:
            flag = False
            results.append(i)
    if flag:
        results.append(f'Работник {employee} не найден')
    return results


def employee_edit(warp, employee, new_employee):
    warp = warp.split('\n')
    id = employee.split(' || ')[0]
    warp[warp.index(employee)] = id + ' || ' + new_employee
    return warp


def employee_delete(warp, result):
    warp = warp.split('\n')
    warp.remove(result)
    return warp
