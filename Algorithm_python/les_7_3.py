"""
Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы,
которые не меньше медианы, в другой – не больше медианы.
Задачу можно решить без сортировки исходного массива.
Но если это слишком сложно, то используйте метод сортировки, который не рассматривался на уроках
"""
import random
m = int(input("Введите коэфициент m, учавствующий в вычислении размера массива: "))
# m = 3
SIZE = 2*m+1
random_array = [i for i in range(SIZE)]
random.shuffle(random_array)
print(f'Исходный массив: {random_array}')

half_array = len(random_array)//2
for i in range(0, len(random_array)):
    count_less = 0
    count_greater = 0
    for j in range(0, len(random_array)):
        if random_array[i] > random_array[j]:
            count_less += 1
        elif random_array[i] < random_array[j]:
            count_greater += 1
    # print(f'{count_less}=={count_greater}')
    if count_less == count_greater:
        print(f'Медиана массива: {random_array[i]}')
        break
