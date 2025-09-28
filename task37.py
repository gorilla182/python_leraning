n = int(input())

matrix = [list(map(int, input().split())) for _ in range(n)]

up_qu = 0
down_qu = 0
left_qu = 0
right_qu = 0

for i in range(n):
    for j in range(n):
        if i < j:
            if i < n-1-j:
                up_qu += matrix[i][j]
            elif i > n-1-j:
                right_qu += matrix[i][j]
        elif i > j:
            if i < n-1-j:
                left_qu += matrix[i][j]
            elif i > n-1-j:
                down_qu += matrix[i][j]
print('Верхняя четверть:', up_qu, '\n', 'Правая четверть:', right_qu, '\n', 'Нижняя четверть:', down_qu, '\n', 'Левая четверть:', left_qu)

