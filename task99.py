from random import randrange as r

tickets = set()

while len(tickets) < 100:
    s = []
    while len(s) < 7:
        s.append(str(r(1, 9)))
    tickets.add(''.join(s))
    s = []

print(*tickets, sep='\n')
