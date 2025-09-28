n = int(input())

matrix = [input().split() for _ in range(n)]

sums = 0

for i in range(n):
    sums += int(matrix[i][i])

print(sums)