choise = int(input("введите число от 1-12: "))
while choise < 1 or choise > 12:
    print("Вы ввели не верное число повторите попытку")
    choise = int(input("введите число от 1-12: "))

month_dict = {
    1: ['January', 'Зима'],
    2: ['February', 'Зима'],
    3: ['March', 'Весна'],
    4: ['April', 'Весна'],
    5: ['May', 'Весна'],
    6: ['June', 'Лето'],
    7: ['Jule', 'Лето'],
    8: ['August', 'Лето'],
    9: ['September', 'Осень'],
    10: ['October', 'Осень'],
    11: ['November', 'Осень'],
    12: ['December', 'Зима']
}
print(f'{month_dict.get(choise)[0]} и это {month_dict[choise][1]}')
