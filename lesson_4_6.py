from itertools import count

for el in count(3):
    if el > 10:
        break
    else:
        print(el)

        """"""

from itertools import cycle

с = 0
list = range(4)

for el in cycle(list):
    if с > 15:
        break
    print(el)
    с += 1
