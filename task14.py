names = ['Руслан', 'Тимур', 'ничья']
res = ['камень', 'ножницы', 'бумага']

timur, ruslan = input(), input()

if ruslan == res[0] and timur == res[1]:
    print (names[0])
elif timur == res[0] and ruslan == res[1]:
    print(names[1])
elif ruslan == res[1] and timur == res[2]:
    print(names[0])
elif timur == res[1] and ruslan == res[2]:
    print(names[1])
elif ruslan == res[2] and timur == res[0]:
    print((names[0]))
elif ruslan == res[0] and timur == res[2]:
    print((names[1]))
elif ruslan == timur:
    print(names[2])