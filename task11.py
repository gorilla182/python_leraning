nums = [int(nums) for nums in input().split()]

num = nums.pop()

nums.insert(0,num)


print(*nums)
