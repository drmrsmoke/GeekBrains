class Road:
    __length = 0
    __width = 0

    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def calc(self):
        print(f"Количество асфальта необходимого для дороги {self.__length * self.__width * 25 * 5 / 1000} тонн")


r = Road(5000, 20)
r.calc()
