from functools import reduce


def my_func(prev, n):
    return prev * n


print(reduce(my_func, [n for n in range(100, 1000) if n % 2 == 0]))
