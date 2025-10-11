a = list(map(int, input().split()))

n, m = a[0], a[1]

matrix = [list(map(int, input().split())) for _ in range(n)]

input()

l = list(map(int, input().split()))

m1, k = l[0], l[1]

matrix2 = [list(map(int, input().split())) for _ in range(m1)]


matrix3 = []

for j in range(n):
    row = []
    for i in range(k):
        h = 0
        for x in range(m):
            h += matrix[j][x]*matrix2[x][i]
        row.append(h)
    matrix3.append(row)



print(matrix3)




