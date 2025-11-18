# put your python code here


from random import randrange as r

matrix = [[0] * 5 for i in range(5)]

used_numbers = set()

for i in range(5):
    for j in range(5):
        if i == j and i == 2:
            matrix[i][j] = 0
            continue

        while True:
            a = r(1, 76)
            if a not in used_numbers:
                used_numbers.add(a)
                matrix[i][j] = a
                break

for i in range(5):
    for j in range(5):
        print(str(matrix[i][j]).ljust(3), end=' ')
    print()