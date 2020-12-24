from math import factorial


def fact(n):
    for i in range(1, n + 1):
        yield factorial(i)


i = True
while i == True:
    try:
        num = int(input("Введите число от которого хотите получить факториал"))
        break
    except ValueError:
        print("Введите целочисленные значения ")

for el in fact(num):
    print(el)
