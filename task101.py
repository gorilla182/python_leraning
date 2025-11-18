from random import shuffle as s
from copy import deepcopy as d

from main import choice

students = {input(): None for _ in range(int(input()))}

names = list(students.keys())

available_names = d(names)



for key in students:

    while True:
        a = choice(available_names)
        if key != a:
            students[key] = a
            available_names.remove(a)
            break


for key, value in students.items():
    print(f'{key} - {value}')



