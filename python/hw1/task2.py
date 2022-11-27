a = [True, False]
b = [True, False]
c = [True, False]
for x in a:
    for y in b:
        for z in c:
            print(x, y, z)
            example1 = not (x or y or z)
            example2 = (not x) and (not y) and (not z)
            print(example1 == example2)
