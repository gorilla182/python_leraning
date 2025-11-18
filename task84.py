
keyboard = {
    1:['.',',','?','!',':'],
    2:['A','B','C'],
    3:['D','E','F'],
    4:['G','H','I'],
    5:['J','K','L'],
    6:['M','N','O'],
    7:['P','Q','R','S'],
    8:['T','U','V'],
    9:['W','X','Y','Z'],
    0: ' '
}

message = [i.upper() for i in input()]

result = []

for i in message:
    for keys, value in keyboard.items():
        if i in value:
            result.append(str(keys)*(value.index(i)+1))

print(*result, sep = '')

