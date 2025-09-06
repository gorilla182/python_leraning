
from math import *


def summ (a,b):
    return a+b
def minus (a,b):
    return a-b
def square (a,b):
    return a*b
def division (a,b):
    return a/b
def int_part (a,b):
    return a//b
def remainder_division(a,b):
    return a%b
def square_sum(a,b):
    return math.sqrt(pow(a,10) + pow(b,10))

a,b = int(input()), int(input())

print(summ(a,b))
print(minus(a,b))
print(square(a,b))
print(division(a,b))
print(int_part(a,b))
print(remainder_division(a,b))
print(square_sum(a,b))

