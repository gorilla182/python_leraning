n, m = int(input()), int(input())

math = {input() for _ in range(n)}
inf = {input() for _ in range(m)}
set1 = math.difference(inf)

print(len(set1))