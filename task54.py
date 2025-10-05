a = list(map(int, input(). split()))

n, m = a[0], a[1]

matrix = [[None] * m for _ in range(n)]
qty = 1

for d in range(n+m-1):
    for i in range(n):
        for j in range(m):
            if i+j == d:
                matrix[i][j] = qty
                qty += 1



for row in matrix:
    print(*row)