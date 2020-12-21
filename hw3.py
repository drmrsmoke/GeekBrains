def my_func(a, b, c):
    res = [a + b, b + c, a + c]
    return max(res)


print(my_func(int(input("a = ")), int(input("b = ")), int(input("c = "))))
