a, b = int(input()), int(input())

matrix = [[0]*b for _ in range(a)]

for i in range(a):
    for j in range(b):
        matrix[i][j] = input()

for i in range(a):
    for j in range(b):
        print(*matrix[i][j], end=' ')
    print()