class Date:
    def __init__(self,day,month,year):
        self.day = day
        self.month = month
        self.year = year
    @classmethod
    def set_data(cls,data):
        d,m,y = data
        try:
            d = int(d)
            m = int(m)
            y = int(y)
        except ValueError:
            print(" Enter only number")
        else:
            return cls (d,m,y)
        finally:
            print ("Finish")

    @staticmethod
    def check_data(obj):
        if obj.day>31 or obj.day<1:
            print("No correct day data")
        elif 12 < obj.month or obj.month <1:
            print("No correct month data")
        else:
            return f"{obj.day}. {obj.month}. {obj.year}"


my_list=[31,12,"2020"]
data = Date.set_data(my_list)
print(f"{Date.check_data(data)}")