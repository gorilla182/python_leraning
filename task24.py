s = input().split()
res = [[s[0]]]
for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        res[-1].append(s[i])
    else:
        res.append([s[i]])
print(res)