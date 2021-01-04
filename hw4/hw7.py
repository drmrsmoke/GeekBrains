from itertools import count, cycle


def generate_number():
    i = False
    while i == False:
        try:
            user_input = int(input("Введите число с которого необходимо начать генерировать числа"))
            break
        except ValueError:
            print("Вы ввели не число")

    i = 0
    numbers = iter(count(user_input))
    while i < user_input + 10:
        print(next(numbers))
        i += 1


def generate_cicle():
    user_input = input(" Введите фразу которую необходимо зациклить")
    i = 0
    cycle_user = iter(cycle(user_input))
    while i < 10:
        print(next(cycle_user))
        i += 1

print("Выберите операци которую хотите произвести ")
print("1: Генератор чисел")
print("2: Цикл из значений")
while True:
    try:
        user_select = int(input("Ваш выбор"))
        if user_select <= 2:
            break
        else:
            print("Выберите 1 или 2")
    except ValueError:
        print("Выберите 1 или 2")
if user_select==1:
    generate_number()
else:
     generate_cicle()
