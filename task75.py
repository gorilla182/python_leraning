n = int(input())
cities = {input() for i in range(n)}

new_city = input()

cities.add(new_city)

print('OK' if len(cities) == n + 1 else 'REPEAT')
