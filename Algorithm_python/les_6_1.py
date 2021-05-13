'''
    Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

    Использую Python 3.9 и Процессорт 64 битный.

    В качестве переменных беру элементы типа int, list, tuple.
    Меньше памяти было выделено в первом варианте, где использую переменные типа int.
    Во втором варианте работаю со списком и под него было выделено гораздо больше памяти, чем для
    int и tuple, так как для списка резервитруется память для дополнительных ячеек.
    Третий вариант - кортеж, так как это неизменяемый тип данных, для него не нужно резервировать
    память под дополнительные ячейки, поэтому он занимает меньше памяти, чем список. Во-вотором и третьем вариантах
    использую встроенную функцию  reduce, и ее не считаю. Алгоритмы работы с кортежем и списком одинаковы,
    хотела посмотреть на выделение памяти для разных типах.
'''
import functools
import sys

# вариант 1: число

# sum_memory = 0
# number = int(input('Введите целое положительное трехзначное число: '))
# sum_memory += sys.getsizeof(number)
# c = number % 10
# b = number % 100 // 10
# a = number // 100
# sum_memory += sys.getsizeof(a)
# sum_memory += sys.getsizeof(b)
# sum_memory += sys.getsizeof(c)
# sum_digits = a + b + c
# product_digits = a * b * c
# sum_memory += sys.getsizeof(sum_digits)
# sum_memory += sys.getsizeof(product_digits)
# print(f'Сумма равна {sum_digits}.'
#       f' Произведение равно {product_digits}.')
# print(f'Под переменные было выделено {sum_memory} байт')
#
# Введите целое положительное трехзначное число: 345
# Сумма равна 12. Произведение равно 60.
# Под переменные было выделено 168 байт


# вариант 2: список

# sum_memory = 0
# number = input('Введите целое положительное трехзначное число: ')
# sum_memory += sys.getsizeof(number)
# lst = []
# for elm in number:
#     lst.append(int(elm))
# sum_memory += sys.getsizeof(lst)
# sum_digits = functools.reduce(lambda x, y: x + y, lst)
# product_digits = functools.reduce(lambda x, y: x * y, lst)
#
# sum_memory += sys.getsizeof(sum_digits)
# sum_memory += sys.getsizeof(product_digits)
# print(f'Сумма равна {sum_digits}.'
#       f' Произведение равно {product_digits}.')
# print(f'Под переменные было выделено {sum_memory} байт')
#
# Введите целое положительное трехзначное число: 345
# Сумма равна 12. Произведение равно 60.
# Под переменные было выделено 196 байт

# вариант 3: кортеж

sum_memory = 0
number = input('Введите целое положительное трехзначное число: ')
sum_memory += sys.getsizeof(number)
tpl = tuple([int(i) for i in number])
sum_memory += sys.getsizeof(tpl)
sum_digits = functools.reduce(lambda x, y: x + y, tpl)
product_digits = functools.reduce(lambda x, y: x * y, tpl)

sum_memory += sys.getsizeof(sum_digits)
sum_memory += sys.getsizeof(product_digits)
print(f'Сумма равна {sum_digits}.'
      f' Произведение равно {product_digits}.')
print(f'Под переменные было выделено {sum_memory} байт')
#
# Введите целое положительное трехзначное число: 345
# Сумма равна 12. Произведение равно 60.
# Под переменные было выделено 172 байт