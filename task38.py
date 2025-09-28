n, m = int(input()), int(input())

matrix = [[i*j for i in range(m)] for j in range(n)]

for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end = ' ')
    print()

