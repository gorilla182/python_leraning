import copy

n = int(input())

matrix = [list(map(int, input().split())) for _ in range(n)]
mirror_matrix = copy.deepcopy(matrix)

for i in range(n):
    mirror_matrix[i].reverse()

for i in range(n):
    for j in range(i + 1, n):
        mirror_matrix[i][j], mirror_matrix[j][i] = mirror_matrix[j][i], mirror_matrix[i][j]

for i in range(n):
    mirror_matrix[i].reverse()

if matrix == mirror_matrix:
    print('YES')
else:
    print('NO')
