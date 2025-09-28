from math import factorial

#n - строка. k - столбец



def pascal (n, k):
    factorials = factorial(n)/(factorial(k)*factorial((n-k)))
    return int(factorials)

def paskal_str(n):
    my_list = []
    for i in range(n+1):
        my_list.append(pascal(n,i))
    return my_list



n = int(input())
print(paskal_str(n))
