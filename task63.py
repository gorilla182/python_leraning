n = int(input())

matrix = [list(map(int, input().split())) for _ in range(n)]

nums = [i for i in range(1, n+1)]
cnt = 0

for i in range(n):
    if nums == sorted(matrix[i]):
        cnt += 1
        for j in range(n):
            if nums[i] in matrix[j][i]:
                cnt += 1

if cnt == n*2:
    print('YES')
else:
    print('NO')
print(cnt)



