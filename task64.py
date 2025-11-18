n = int(input())

matrix = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        else:
            matrix[i][j] = j-i
for row in matrix:
    print(*row)
