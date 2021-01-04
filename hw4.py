translate = {"One" : "Один", "Two": "Два","Three": "Три", "Four": "Четыре"}
new_file = []
with open("text_4.txt", "r", encoding="utf-8") as read_file:
    for i in read_file:
        i = i.split(' ' , 1)
        new_file.append(translate[i[0]] + ' '+ i[1])
with open("text_4_ru.txt", "w", encoding="utf-8" ) as ru_file:
    ru_file.writelines(new_file)
    print("Файл создан")

