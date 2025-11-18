n = int(input())

nicknames = [input().split(":") for _ in range(n)]

result = set()
cnt = 0

for i in range(len(nicknames)):
    if nicknames[i][1] == ' Correct':
        cnt+=1
        result.add(nicknames[i][0])

percent = round((cnt/n * 100))

print('Верно решили', len(result), 'учащихся')
print('Из всех попыток', str(percent)+'%' ,'верных')

