n, m = int(input()), int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

maximum = max(max(matrix, key=max))

for i in range(n):
    for j in range(m):
        if matrix[i][j] == maximum:
            print(i, j)
            break  # прерываем внутренний цикл
    else:
        continue  # если не нашли в этой строке, продолжаем
    break  # прерываем внешний цикл
