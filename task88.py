lst = [word.strip('.,!?:;-') for word in input().lower().split()]

result = {}

for i in lst:
    result[i] = result.get(i, 0)+1

min_wrds = min(result.values())


