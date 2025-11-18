n = int(input())

mylist = []
cnt = 0

for i in range(n):
    if cnt < 3:
        mylist.append(1)
        cnt+=1
    else:
        x = mylist[i-1]+mylist[i-2]+mylist[i-3]
        mylist.append(x)

print(mylist)