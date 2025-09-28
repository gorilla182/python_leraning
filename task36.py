n = int(input())

matrix = [list(map(int, input().split())) for _ in range(n)]

largest1 = matrix[0][0]
largest2 = matrix[-1][-1]

for i in range(n):
    for j in range(n):
        if (i >= j and i <= n-1-j) and matrix[i][j] > largest1:
            largest = matrix[i][j]

for i in range(n):
    for j in range(n):
        if (i <= j and i > (n-1-j)) and matrix[i][j] > largest2:
            largest2 = matrix[i][j]

print(max(largest1, largest2))

