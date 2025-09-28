n = int(input())

matrix = [input().split() for _ in range(n)]
for i in range(n):
    for j in range(n):
        matrix[i][j] = int(matrix[i][j])

for i in range(n):
    sums = 0
    cnt = 0
    for j in range(n):
        sums += matrix[i][j]
    sums = sums / n
    for j in range(n):
        if float(matrix[i][j]) > sums:
            cnt += 1
    print(cnt)