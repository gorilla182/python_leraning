n = 4

sosi = ['s', 'o', 's', 'i']
huec = ['h', 'u', 'e', 'c']


matrix = [[0]*n for _ in range(n)]

for i in range(n):
    matrix[i][i] = sosi[i]
    matrix[i][n-1-i] = huec[i]

for i in range(n):
    for j in range(n):
        print(matrix[i][j], end = ' ')
    print()