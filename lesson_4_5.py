from functools import reduce


def my_func(p_el, el):
    return p_el * el


new_list = [el for el in range(99, 1001) if el % 2 == 0]
print(new_list)
print(reduce(my_func, new_list))
