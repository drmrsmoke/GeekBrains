def my_func():
    sum = 0
    while True:
        user_input = input("введите цифры через пробел или введите q").split()
        current = 0
        for i in user_input:
            if i =="q":
                print(f"Сумма введенных чисел {sum}")
                return
            else:
                current+=int(i)
                sum+=int(i)
        print(f"Сумма чисел {current} общая сумма чисел {sum}")
my_func()