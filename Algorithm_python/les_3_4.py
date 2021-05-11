"""
    В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
"""
import random

SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)
m = 0
for i in range(len(array)):
    if array[i] < 0:
        min_ = abs(array[0])
        if abs(array[i]) < min_:
            min_ = abs(array[i])
            m = i
print(f'Максимальный отрицательный элемент = -{min_}, его позиция в массиве {m}')
