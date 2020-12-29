with open("text5.txt", "w", encoding="utf-8" ) as file:
    #todo try except
    num =  input("Введите числа разделенные пробелом")
    file.write(num)
    num = num.split()
    print (f"Сумма введенных чисел равна {sum(map(float,num))}")