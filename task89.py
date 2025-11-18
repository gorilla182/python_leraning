list_words = [input().split(': ') for _ in range (int(input()))]

dictionary = {}

for i in range(len(list_words)):
    for j in range(len(list_words[i])):
        dictionary[list_words[i][0]] = dictionary.setdefault(list_words[i][0],list_words[i][1])

zapros = [input().capitalize() for i in range(int(input()))]


for s in zapros:
    if s in dictionary:
        val = dictionary.get(s, 'Не найдено')
        print(val)
