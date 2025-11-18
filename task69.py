nums = input().split()
numbers = set()
qty = 0

for i in range(len(nums)):
    nums[i] = nums[i].lstrip('0')
    numbers.add(nums[i])
    if len(nums) == qty:
        print('NO')
    else:
        print('YES')
    qty += 1



print(nums)