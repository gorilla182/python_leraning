set1 = set(map(int, input().split()))
set2 = set(map(int, input().split()))
set3 = set(map(int, input().split()))

union_set = set1|set2|set3
intersection_set = set1&set2&set3
s4 = union_set.difference(intersection_set)

print(s4)