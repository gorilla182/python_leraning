
words = input().split()
word = set()

for i in range(len(words)):
    if words[i].endswith(('.', ',', ';', ':', '-', '?', '!')):
        words[i].removesuffix(words[i])


for i in words:
    word.add(i.lower())

print(len(word))
print(word)

