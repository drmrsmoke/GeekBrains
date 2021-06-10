import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

key = []
for i, k in enumerate(array):
     if k%2==0:
         key.append(i)
print(key)