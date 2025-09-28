n = int(input())

matrix = [list(map(int, input().split())) for _ in range(n)]

cnt = 0

for i in range(n):
    sq = []
    ls = []
    for j in range(n):
        sq.append(matrix[i][0])
        ls.append(matrix[i][-1])

    if matrix[0] == sq and matrix[-1] == ls:
        print('YES')
    else:
        print('NO')

