month = [None, ["january", "зимний"], ["february", "зимний"], ["march", "весенний"], ["april", "весенний"],
         ["may", "весенний"], ["june", "летний"], ["july", "летний"], ["august", "летний"], ["september", "осенний"],
         ["october", "осенний"], ["november", "осенний"], ["december", "зимний"]]
choise = int(input("введите число от 1-12"))
while choise < 1 or choise > 12:
    print("Вы ввели не верное число повторите попытку")
    choise = int(input("введите число от 1-12"))
print(f"вы выбрали {choise} месяц и это {month[choise][0]} {month[choise][1]} месяц ")
