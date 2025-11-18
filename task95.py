dct = {}

for _ in range(int(input())):
    s = input().split()
    name = s[0]
    goods = s[1]
    qty = s[2]
    dct.setdefault(name, {goods : qty})

print(dct)

