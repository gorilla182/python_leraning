n = int(input())
matrix = [list(map(int, input().split())) for i in range(n)]

for i in range(n):
    for j in range(n):
        matrix[i][i], matrix[n-i-1] = matrix[n-i-1], matrix[i]

for row in matrix:
    print(*row)