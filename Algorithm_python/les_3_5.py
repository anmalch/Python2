"""
     В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
     Сами минимальный и максимальный элементы в сумму не включать.
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
print(f'Минимальный элемент = {min_}')

max_ = array[0]
max_index = 0
for i in range(len(array)):
    if array[i] > max_:
        max_ = array[i]
        max_index = i
print(f'Максимальный элемент = {max_}')
s = 0
if min_index < max_index:
    for i in range(min_index+1, max_index):

        s += array[i]
    print(f'Сумма = {s}')
else:
    for i in range(max_index+1, min_index):

        s += array[i]
    print(f'Сумма равна {s}')