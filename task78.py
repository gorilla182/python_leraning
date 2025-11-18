m, n = int(input()), int(input())

math = {input() for _ in range(m)}
inf = {input() for _ in range(n)}
set1 = math.symmetric_difference(inf)

if len(set1) == 0:
    print('NO')

else:
    print(len(set1))