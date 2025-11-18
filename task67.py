n = int(input())

word = []
words = set()
for i in range(n):
    words = set(input().lower())
    word.append(list(words))

for i in word:
    words.add(i)

print(len(word))
print(word)
