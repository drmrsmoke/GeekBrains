list_user = []
temp = 0
while True:
    temp = input("введите значение для списка через enter, после окончания ввода нажмите q ")
    if temp == "q":
        break
    else:
        list_user.append(temp)
print(list_user)
length_temp = len(list_user)
if length_temp % 2 == 0:
    for i in range(0, len(list_user), 2):
        list_user[i], list_user[i + 1] = list_user[i + 1], list_user[i]
elif length_temp % 2 != 0:
    for i in range(0, len(list_user) - 1, 2):
        list_user[i], list_user[i + 1] = list_user[i + 1], list_user[i]

print(list_user)
