class Check_list:
    def __init__(self):
        self.my_list = []

    def user_input(self):
        while True:
            try:
                num = int(input("Введите значение - "))
                self.my_list.append(num)
                print(f"Список введенный вами {self.my_list}\n")
            except(ValueError):
                print("Вводите только числа ")
                exit_question = input("Хотите выйти Y/N").upper()
                if exit_question == "Y":
                    return "Finish"
                else:
                    try_except.user_input
try_except=Check_list()
print(try_except.user_input())

