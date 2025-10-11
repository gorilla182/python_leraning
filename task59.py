n = int(input())

matrix = [list(map(int, input().split())) for _ in range(n)]

elem = []

for i in range(n):
    for j in range(n):
        if i<j and i>= n-1-j:
            elem.append(matrix[i][j])
        elif i > j and i >= n-1-j:
            elem.append(matrix[i][j])

print(max(elem))
