from abc import ABC, abstractmethod
class Cloth:

    def __init__(self, width, high):
        self.my_width = width
        self.my_hight = high

    @abstractmethod
    def textil_square(self):
        pass

    @property
    def return_square(self):
        return f"Площадь ткани равна {self.total_square}"


class Suit(Cloth):
    def textil_square(self):
        self.total_square = 2*self.my_hight+0,3
        return self.return_square
        #return f"Количество ткани потраченное на костюм {2*self.my_hight+0,3}"

class Jaket(Cloth):
    def textil_square(self):
        self.total_square = self.my_width/6,5+0,5
        return self.return_square

my_suit = Suit(16,14)
print(my_suit.textil_square())
my_suit = Jaket(16,14)
print(my_suit.textil_square())

