def prime_numbers(n: int, new: bool = False) -> list[int]:
    i = 2
    ListOfNums = []
    while n != 1:
        while n % i == 0:
            ListOfNums.append(i)
            n //= i
        i += 1
    if new:
        return list(set(ListOfNums))
    else:
        return ListOfNums


n = int(input("Введите число: "))
print(f"Простые множители числа  приведены в списке: {prime_numbers(n, True)}")
