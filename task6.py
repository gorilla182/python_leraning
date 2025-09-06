def rotate(s):
    if len(s) == 5:
        return int(s[::-1])
    elif len(s) == 6:
        return (s[0]) + int(rotate(s[1::]))

s = input()
print(rotate(s))
