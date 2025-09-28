n, m = int(input()), int(input())
#a[i][столбец1], a[i][столбец2] = a[i][столбец2], a[i][столбец1]

matrix = [list(map(int, input().split())) for _ in range(n)]
column = [list(map(int, input().split()))]
j1 = column[0]
j2 = column[1]
for i in range(n):
    for j in range(m):
        matrix[i][j1], matrix[i][j2] = matrix[i][j2], matrix[i][j1]

for i in range(n):
    for j in range(m):
        print(matrix[i][j], end = ' ')
    print()