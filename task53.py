a = list(map(int, input().split()))

n, m = a[0], a[1]

matrix = [[None]* m for _ in range(n)]

cnt = 1


for i in range (n):
    for j in range(m):
        matrix[i][j] = cnt
        cnt+=1

for i in range(n):
    if i %2 != 0:
        matrix[i].reverse()
for row in matrix:
    print(*row)
