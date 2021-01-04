import json
forma = {}
form_average ={}
average = 0
fin_list = []
with open("text_7.txt", "r", encoding="utf-8") as file_read:
    for firm in file_read:
        name, form, dohod, izdrzhki = firm.split()
        forma[name] = int(dohod) - int(izdrzhki)
        average = average + forma.setdefault(name)
    form_average['average_profit'] = average
    fin_list = [forma,form_average]
    print(fin_list)
with open("text_77.json", "w", encoding="utf-8") as write_json:
    json.dump(fin_list, write_json )