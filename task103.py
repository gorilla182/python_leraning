from decimal import *
num = Decimal(input())

nums = num.as_tuple()

nums_list = list(nums[1])

if 0 not in nums_list:
    nums_list.append(0)

print(min(nums_list)+max(nums_list))
