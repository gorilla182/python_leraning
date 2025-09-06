n = int(input())
nums = [int(input()) for i in range(n)]
res = 'НЕТ'
sqrt = int(input())

for i in range(0, n):
    for j in range (0, n):
        if i != j:
            if nums[i] * nums[j] == sqrt:
                res = 'ДА'
                break

print(res)