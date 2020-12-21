def int_func(s):
    words = s.split()
    ret = []
    for i in words:
        if i.isalpha(): #проверяю что текст
            c = 0
            ret.append(" ") # разделитель между словами
            while c<len(i):
               for el in i:
                    if ord(el) >97 and ord(el) < 122: #проверяем на латиницу
                        ret.append(el)
                        c+=1
                    else:
                        c+=1


    print("".join(ret).title())
text = input("Введите текст для преобразования")
int_func(text)