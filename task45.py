n = int(input())

matrix = [list(map(int, input().split())) for _ in range(n)]

flagstr = False

cnt = sum(matrix[0])
cnt2 = 0
cnt3 = 0


diag1 = 0
diag2 = 0

for i in range(n):
    for j in range(n):
        diag1 += matrix[i][i]
        diag2 += matrix[i][n-i-1]
        if matrix[j][i] == cnt:
            cnt3 += 1


for i in range(n):
    if sum(matrix[i]) == cnt:
        cnt2 +=1

if cnt2 == len(matrix):
    flagstr = True

if cnt == cnt2 == cnt3 == diag1 == diag2:
    print('YES')
else:
    print('NO')

print(diag1)
print(diag2)
print(cnt)
print(cnt2)
print(cnt3)

