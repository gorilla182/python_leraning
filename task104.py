from fractions import Fraction as F

a, b = input(), input()

print(f'{F(a)} + {F(b)} = {F(a)+F(b)}'
f'{F(a)} - {F(b)} = {F(a)-F(b)}'
f'{F(a)} * {F(b)} = {F(a)*F(b)}'
f'{F(a)} / {F(b)} = {F(a)/F(b)}', sep = '\n')