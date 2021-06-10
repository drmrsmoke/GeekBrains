"""""
https://drive.google.com/file/d/1NwQtPyRCKYT2VSKwt-vCuuguWbO1oYvB/view?usp=sharing

Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.


"""


num = input('Введите трехзначное число:\n')

if num.isdigit():
    if len(num) != 3:
        print('Нужно ввести 3х значное число.')
    else:
        mult = 1
        summ = 0
        for i in num:
            summ += int(i)
            mult *= int(i)
        print(f'Сумма цифр цисла {num} = {summ}, произведение = {mult}')
else:
    print('Введите ЧИСЛО согласно условию')