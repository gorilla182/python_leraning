a = list(map(int, input().split()))

n = a[0]
m = a[1]


nums = [i for i in range(1, m+1)]
matrix = []



for i in range(n):
    matrix.append(nums.copy())
    a = nums.pop(0)
    nums.append(a)



for row in matrix:
    print(*row)
