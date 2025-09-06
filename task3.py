def string_price(string):
    cnt = len(string)*60
    rubles = cnt//100
    cent = cnt%100
    print (rubles, 'р.',cent, 'коп.')

text = input()
string_price(text)

