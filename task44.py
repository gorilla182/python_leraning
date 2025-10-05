n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

# Создаем транспонированную матрицу
transposed = [[matrix[j][i] for j in range(n)] for i in range(n)]

for i in range(n):
    transposed[i].reverse()
    print(*transposed[i], end='\n')
