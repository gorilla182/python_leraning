import random
from random import choice


def generate_ip():
    return '.'.join(str(choice(range(256))) for _ in range(4))


print(generate_ip())