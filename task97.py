from  string import ascii_uppercase as s
from random import choice as c
from random import randrange as r


def generate_index():
    return f'{c(s)}{c(s)}{r(99)}_{r(99)}{c(s)}{c(s)}'

print(generate_index())