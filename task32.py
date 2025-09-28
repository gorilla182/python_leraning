a, b = int(input()), int(input())

matrix = [[input() for _ in range(b)] for _ in range(a)]

for i in matrix:
    print(*i)
print()

for i in range(a):
    for j in range(b):
        print(matrix[j][i], end = ' ')
    print()