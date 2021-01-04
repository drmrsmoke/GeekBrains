import random

class car:
    side  = ["right", "left"]

    def __init__(self, s, c, n, iPo):
        self.speed = s
        self.color = c
        self.name = n
        self.isPolice = bool(iPo)
    def go(self):
        print(f"{self.name} поехала ")
        if self.isPolice == True:
            print("piu-piu")

    def stop(self):
        print(f"{self.name} остановилась")

    def turn(self):
        direction = random.choice(self.side)
        print(f"{self.name} повернула {direction}")

    def ShowSpeed(self):
        print(f"Скорость автомобиля {self.speed}")




class TownCar(car):
    def ShowSpeed(self):
        if self.speed > 60:
            print("Вы привысили скорость")
        else:
            print(f"Скорость автомобиля {self.speed}")


class WorkCar(car):
    def ShowSpeed(self):
        if self.speed > 40:
            print("Вы привысили скорость")
        else:
            print(f"Скорость автомобиля {self.speed}")


class SportCar(car):
    pass


class PoliceCar(car):
    pass


t = TownCar(65, "green", "Mazda",0)
t.go()
t.turn()
t.ShowSpeed()
p= PoliceCar(65, "Black and White", "Chevrolet",1)
p.go()
p.turn()
p.ShowSpeed()
w = WorkCar(35, "Yellow", "Ford", False)
w.go()
w.turn()
w.ShowSpeed()
s= SportCar(250, "RED", "Porshe", False)
s.go()
s.turn()
s.turn()
s.ShowSpeed()