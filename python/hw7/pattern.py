def contact_search(warp, contact):
    warp = warp.split('\n')
    flag = True
    results = []
    for i in warp:
        if contact in i:
            flag = False
            results.append(i)
    if flag:
        results.append(f'Контакт {contact} не найден')
    return results
