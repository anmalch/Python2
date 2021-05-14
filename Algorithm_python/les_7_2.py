"""
Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50).
Выведите на экран исходный и отсортированный массивы.
"""
import numpy

SIZE = 7
array = numpy.random.random(SIZE) * 50
print(f'Исходный массив: {array}')


def merge_func(list1, list2):
    merged_list = []
    i = 0
    j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1

    if i == len(list1):
        merged_list.extend(list2[j:])

    elif j == len(list2):
        merged_list.extend(list1[i:])

    return merged_list


def merge_sorted(arr):
    if len(arr) == 1:
        return arr
    else:
        left_array = arr[:len(arr) // 2]
        right_array = arr[len(arr) // 2:]

        left_sorted = merge_sorted(left_array)
        right_sorted = merge_sorted(right_array)

        return merge_func(left_sorted, right_sorted)


print(f' Отсортированный массив: {merge_sorted(array)}')
