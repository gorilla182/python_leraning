first_word = input().strip('.,!?:;- ').replace(' ', '')
second_word = input().strip('.,!?:;- ')
if first_word == second_word:
    print('YES')
else:
    print('NO')