ZP = []
min_zp = []
min_zp_name = []
with open("text_3.txt", "r", encoding="utf-8") as user_list:
    user_file = user_list.read().split('\n')
    for i in user_file:
        i = i.split()
        ZP.append(float(i[1]))
        if float(i[1]) < 20000:
            min_zp.append(i[1])
            min_zp_name.append(i[0])
res = zip(min_zp_name, min_zp)
res_list = list(res)
print("Сотрудники у которых зп меньше 20 000")
for i in res_list:
    print(f" {i[0]} - {i[1]}")
print(f"Средняя зп по компании: {sum(map(float, ZP)) / len(ZP)}")
