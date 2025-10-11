a = list(map(int, input().split()))

n, m = a[0], a[1]

matrix = [list(map(int, input().split())) for _ in range(n)]

matrix2 = [list(map(int, input().split())) for _ in range(n)]

c = []

for i in range(n):
    row = []
    for j in range(m):
        r = matrix[i][j]+matrix2[i][j]
        row.append(r)
    c.append(row)

for row in c:
    print(*row)