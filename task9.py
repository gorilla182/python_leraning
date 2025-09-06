nums = input()
cnt = 0


nums_list = [int(nums) for nums in nums.split()]

for i in range(1, len(nums_list)):
    if nums_list[i] > nums_list[i-1]:
        cnt+=1



print(cnt)

