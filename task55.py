
a = list(map(int, input().split()))

n, m = a[0], a[1]

matrix = [[None]*m for _ in range(n)]

#for d in range((n+m)-1):
    #for i in range(m):
        #for j in range(n):


directions = ['left', 'down', 'right', 'up']
i, j = 0, 0
current_direction = 'right'
cnt = 1

for _ in range(n*m):
    if current_direction == 'right':
        matrix[i][j] = cnt
        cnt += 1
        j+=1
        if j == m-1:
            current_direction = 'down'
    elif current_direction == 'down':
        matrix[i][j] = cnt
        cnt+=1
        i+=1
        if i == n-1:
            current_direction = 'left'
    elif current_direction == 'left':
        matrix[i][j] = cnt
        cnt += 1
        j -= 1
        if j == 0:
            current_direction = 'up'
    elif current_direction == 'up':
        matrix[i][j] = cnt
        cnt += 1
        i -= 1
        if i == 1:
            current_direction = 'right'





for row in matrix:
    print(*row)