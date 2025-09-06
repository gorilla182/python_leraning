nums = [int(nums) for nums in input().split()]

if len(nums)%2 == 0:
    for i in range(1, len(nums), 2):
        nums[i], nums[i-1] = nums[i-1], nums[i]
    print(*nums)
elif len(nums)%2 != 0:
    for i in range(1, len(nums)-1, 2):
        nums[i], nums[i - 1] = nums[i - 1], nums[i]
    print(*nums)