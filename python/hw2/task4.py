with open('file.txt', 'r') as f:
    pos = f.read().split('\n')
pos = list(map(int, pos))

n = int(input())
ListOfNum = [i for i in range(-n, n+1)]
MultOfList = 1
for k in pos:
    MultOfList *= ListOfNum[k]

print(pos)
print(ListOfNum)
print(MultOfList)
