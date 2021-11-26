from math import factorial
from itertools import count


def generator():
    for el in count(1):
        yield factorial(el)


n = 0
for i in generator():
    if n == 5:
        break
    else:
        n += 1
        print(f"Факториал {n} = {i}")
