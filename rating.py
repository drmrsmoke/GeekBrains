my_list = [7, 5, 3, 3, 2]
num = int(input("Введите число"))
my_list.insert(0, num) if num > my_list[0] else my_list.insert(-my_list[::-1].index(num),num) if num in my_list else my_list.append(num)


if num >my_list[0]:
    my_list.insert(0,num)
elif num in my_list:
    my_list.insert(-my_list[::-1].index(num), float(num))
else:
    my_list.append(num)

print(my_list)