m, n = int(input()), int(input())

a = [input() in range(m+n)]

b = set(a)

c = (len(a)-len(b))*2

print(m+n - c)