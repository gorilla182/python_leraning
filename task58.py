n = int(input())
matrixA = [list(map(int, input().split())) for _ in range(n)]
m = int(input())

# Начинаем с единичной матрицы для степени 1
result = [row[:] for row in matrixA]  # глубокое копирование

for power in range(1, m):
	temp = [[0] * n for _ in range(n)]

	for i in range(n):
		for j in range(n):
			total = 0
			for k in range(n):
				total += result[i][k] * matrixA[k][j]
			temp[i][j] = total

	result = temp

# Вывод результата
for row in result:
	print(*row)

