n = int(input())

strings = [input() for i in range(n)]
damaged = []

for i in range(n):
    s = strings[i]
    target = 'anton'
    index = 0

    for j in s:
        if index < len(target) and j  == target[index]:
            index += 1
    if index == len(target):
        damaged.append((i+1))

print(*damaged)