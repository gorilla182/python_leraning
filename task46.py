a = list(map(int, input().split()))

n, m = a[0], a[1]

matrix = [['.']*m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if (i+j)%2 != 0:
            matrix[i][j] = '*'

for row in matrix:
    print(*row)

