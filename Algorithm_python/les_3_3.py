"""
    В массиве случайных целых чисел поменять местами минимальный и максимальный элементы
"""
import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

min_ = array[0]
min_index = 0
for i in range(len(array)):
    if array[i] < min_:
        min_ = array[i]
        min_index = i
print(f'минимальный элемент = {min_}')

max_ = array[0]
max_index = 0
for i in range(len(array)):
    if array[i] > max_:
        max_ = array[i]
        max_index = i
print(f'максимальный элемент = {max_}')

array[min_index], array[max_index] = array[max_index], array[min_index]
print(array)