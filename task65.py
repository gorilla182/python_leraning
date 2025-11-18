n = int(input())

names = [tuple(input().split()) for _ in range(n)]

names = tuple(names)

for i in names:
    print(*i)

print()

for i in range(n):
    if names[i][1] == '4' or names[i][1] == '5':
        print(*names[i])
