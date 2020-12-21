def devision(a, b):
    try:
        return a / b
    except ZeroDivisionError as ex:
        print(f'Error: {ex} ')

print(devision(4,0))
