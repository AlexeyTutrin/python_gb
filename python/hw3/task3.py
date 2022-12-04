array = [1.1, 1.2, 3.1, 5, 10.01]
operation = [round(i % 1, 2) for i in array if i % 1 != 0]
print(max(operation) - min(operation))
