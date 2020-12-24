from sys import argv

file,stavka, time, bonus = argv
print("File name", file)
print("Ставка : ", stavka)
print("Часов отработано: ", time)
print("Премия: ", bonus)
print(f"Зароботная плата состовляет {(int(stavka)*int(time))+int(bonus)} золотых слитка")