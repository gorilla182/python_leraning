from math import factorial

#n - строка. k - столбец



def pascal (n, k):
    factorials = factorial(n)/(factorial(k)*factorial((n-k)))
    return int(factorials)

def paskal_str(n):
    my_list = []

    for i in range(n):
        elem = []
        for j in range(i+1):
            elem.append(pascal(i,j))
        my_list.append(elem)



    return my_list



n = int(input())

my_list = paskal_str(n)

for _ in my_list:
    for elem in _:
        print(elem, end = ' ')
    print()
