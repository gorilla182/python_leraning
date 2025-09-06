nums = [int(nums) for nums in input().split()]

def find(lists):
    cnt = 0
    for i in range(len(lists)):
        if lists[i-1] != lists[i]:
            cnt +=1
    if len(lists) == 1:
        cnt = 1
    return cnt

print(find(nums))