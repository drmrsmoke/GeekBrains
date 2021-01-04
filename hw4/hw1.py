from sys import argv
def budget():
    file, stavka, time, bonus = argv
    try:
        int(stavka)
        float(time)
        int(bonus)
    except ValueError:
        return print("Введите корректныке данные")

    print("File name", file)
    print("Ставка : ", stavka)
    print("Часов отработано: ", time)
    print("Премия: ", bonus)
    print(f"Зароботная плата состовляет {(int(stavka) * int(time)) + int(bonus)} золотых слитка")
budget()