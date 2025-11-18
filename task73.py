set1 = set(map(int, input().split()))
set2 = set(map(int, input().split()))
set3 = set(map(int, input().split()))
set4 = {0,1,2,3,4,5,6,7,8,9,10}

set_union = (set1|set2|set3|set4) - (set1|set2|set3)

print(set_union)