a = list(map(int, input().split()))

n, m = a[0], a[1]

matrix = [[None]* m for _ in range(n)]
counter = 1

for j in range(m):
    for i in range(n):
        matrix[i][j] = counter
        counter += 1

for row in matrix:
    print(*row)
