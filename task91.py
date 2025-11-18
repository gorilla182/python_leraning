mydict = {}

for _ in range(int(input())):
    number, name = input().split()
    mydict.setdefault(name,[]).append(number)


print(mydict)