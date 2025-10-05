a = list(map(int, input().split()))

n, m = a[0], a[1]

matrix = [[None] * m for _ in range(n)]

nums = [i for i in range(1, (n*m)+1)]

for i in range(n):
    for j in range(m):
        matrix[i][j]  = nums[i*m+j]

print(matrix)