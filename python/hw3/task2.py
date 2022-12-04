def MultArray(array):
    a = len(array)//2 + 1
    NewArray = [array[i]*array[len(array)-i-1] for i in range(a)]
    print(NewArray)


array = [3, 2, 4, 5, 6]
MultArray(array)
