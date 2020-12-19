phrase_from_user=input("Введите фразу для разбиения на слова")
word_tr = phrase_from_user.split()
for num, i in enumerate(word_tr):
    if len(i)>10:
        print(num, i[:10:])
    else:
        print(num,i)