class worker:
    name = ''
    surname = ''
    position = ''
    wage = 0
    bonus = 0


class Position(worker):
    def __init__(self, name, surname, wage, bonus):
        self.name = name
        self.surname = surname
        self.__income = {"wage": wage, "bonus": bonus}

    def get_full_name(self):
        return self.name + self.surname

    def get_total_income(self):
        return self.__income["wage"] + self.__income["bonus"]


p = Position("Ivan", "Ivanov", 20000, 500)

print(f"Ваше полное имя {p.get_full_name()} и ваш оклад составляет {p.get_total_income()}")
