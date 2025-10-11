n = int(input())

matrix = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        matrix[i][j], matrix[j][i] = matrix[i][j], matrix[i][j]

for row in matrix:
    print(*row)