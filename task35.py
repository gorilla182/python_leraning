n = int(input())

matrix = [list(map(int, input().split())) for _ in range(n)]

matrix2 = []
for i in range(n):
    matrix2.append(matrix[i][0:i + 1])

maxi = -100000000000

for i in range(len(matrix2)):
    for j in range(len(matrix2[i])):
        if matrix2[i][j] > maxi:
            maxi = matrix2[i][j]



print(maxi)
