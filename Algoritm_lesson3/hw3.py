import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

mn = 0
mx = 0
for i in range(0, len(array)):
    if array[i] < array[mn]:
        mn = i
    elif array[i] > array[mx]:
        mx = i
print('arr[%d]=%d arr[%d]=%d' % (mn + 1, array[mn], mx + 1, array[mx]))
b = array[mn]
array[mn] = array[mx]
array[mx] = b
print(array)

