def SumArray(a: list[int]) -> int:
    return sum(a[1::2])


array = [2, 3, 5, 8, 3]
print(SumArray(array))
