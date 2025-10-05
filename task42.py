n = int(input())

matrix = [list(map(int, input().split())) for _ in range(n)]

j = int(n/2)
for i in range(j):
    if i > 0:
        j = i*(-1) - 1
        matrix[i],matrix[j] = matrix[j],matrix[i]
    elif i == 0:
        matrix[i],matrix[-1] = matrix[-1],matrix[i]

for i in range(n):
    for j in range(n):
        print(matrix[i][j], end = ' ')
    print()
