def chunked(words, chunk):
    elem = []
    for i in range(0,len(words), chunk):
        elem.append(words[i:i+chunk])
    return elem

word = input().split()
n = int(input())

print(chunked(word, n))

