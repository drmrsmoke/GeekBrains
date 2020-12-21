def my_func(osnova, stepen):
    R = 1
    if stepen == 0: return 1
    if osnova == 0: return 0
    while stepen > 0:
        R *= osnova
        stepen -= 1
    return 1 / R
print(my_func(int(input('Основание')), int(input('Степень'))))