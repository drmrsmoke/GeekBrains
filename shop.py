full_dict = []
analytics = {'name': [], 'price': [], 'quantity': [], 'unit': []}
n = 0
# Наполнение базы товарами
while True:
    print("_" * 30)
    user_input = input("Нажмите Enter для добавления товара или нажмите Q для перехода к аналитике склада ").upper()
    if user_input == "Q" or user_input == "Й":
        break
    n += 1
    name = input('Введите наименоване товара: ')
    price = int(input('Введите цену товара: '))
    quantity = int(input('Введите количество товара: '))
    unit = input('Введите еденицу измерения: ')
    full_dict.append((n, {'name': name, 'price': price, 'quantity': quantity, 'unit': unit}))

# Заполнение базы аналитики
for good in full_dict:
    for k ,v in good[1].items():
        analytics[k].append(v)
enter = 0

# Заведение меню и настройка всяких красивостей
while True:
    print("Нажмите 1 чтобы получить только список товара")
    print("Нажмите 2 чтобы получить только цену товара")
    print("Нажмите 3 чтобы получить только количество товара")
    print("Нажмите 4 чтобы получить полную аналитику")
    print("Нажмите 5 чтобы выйти из программы")
    enter = int(input("Ваш выбор: "))
    print("_" * 30)
    if 5<enter or enter<1:
        print("Выбор сделан не верно повторите попытку")
        print("_" * 30)
        continue
    if enter == 5:
        break
    if enter == 1:
        print(f"Наименование товара у вас на складе {analytics['name']}")
        print("_" * 30)
    if enter == 2:
        print(f"Цена товара у вас на складе {analytics['price']}")
        print("_" * 30)
    if enter == 3:
        print(f"Количество товара у вас на складе {analytics['quantity']} {analytics['unit']}")
        print("_"*30)
    if enter == 4:
        for k,v in analytics.items():
            print(f"{k[:25]:>30}:{v}")
        print("_" * 30)











    # n += 1
    # for f in features.keys():
    #     user_input = input(f"Введите значение{f}")
    #     features[f] = int(user_input) if f == 'price' or f == 'quantity' else user_input
    # full_dict.append((n, features))
    # print(f"Структура товара {full_dict}")


