class MyEx(Exception):
    def __init__(self, text):
        self.text = text

num=input("Веедите делитель: ")

try:

    num= int(num)
    if num == 0:
        raise MyEx("Делить на ноль запрещено: ")
    res = 100 / num
except (ValueError, MyEx) as err:
    print(err)
else:
    print(res)