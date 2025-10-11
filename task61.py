n = int(input())

matrix = [['.'] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == j:
            matrix[i][j] = '*'
        matrix[i][int(n/2+0.5)] = '*'


for row in matrix:
    print(*row)