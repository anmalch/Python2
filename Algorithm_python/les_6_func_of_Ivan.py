"""
    Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

    Использую Python 3.9 и Процессорт 64 битный.
    В качестве переменных беру элементы типа int, list, tuple.
    Меньше памяти было выделено в первом варианте, где использую переменные типа int.
    Во втором варианте работаю со списком и под него было выделено гораздо больше памяти, чем для
    int и tuple, так как для списка резервитруется память для дополнительных ячеек.
    Третий вариант - кортеж, так как это неизменяемый тип данных, для него не нужно резервировать
    память под дополнительные ячейки, поэтому он занимает меньше памяти, чем список.

"""
import functools

from summ import SumMemory

# вариант 1:

# number = int(input('Введите целое положительное трехзначное число: '))
# c = number % 10
# b = number % 100 // 10
# a = number // 100
# sum_digits = a + b + c
# product_digits = a * b * c
# print(f'Сумма равна {sum_digits}.'
#       f' Произведение равно {product_digits}.')
#
# sum_mem = SumMemory()
# sum_mem.extend(number, a, b, c, sum_digits, product_digits)
# print(sum_mem)

# Введите целое положительное трехзначное число: 345
# Сумма равна 12. Произведение равно 60.
# Объекты класса <class 'int'> в количестве 6 заняли 168 байт


# вариант 2: со списком
number = input('Введите целое положительное трехзначное число: ')
lst = []
for elm in number:
    lst.append(int(elm))

sum_digits = functools.reduce(lambda x, y: x + y, lst)
product_digits = functools.reduce(lambda x, y: x * y, lst)
print(f'Сумма равна {sum_digits}.'
      f' Произведение равно {product_digits}.')

sum_mem = SumMemory()
sum_mem.extend(number, lst, sum_digits, product_digits)
print(sum_mem)

# Введите целое положительное трехзначное число: 345
# Объекты класса <class 'str'> в количестве 1 заняли 52 байт
# Переменные заняли в сумме 280 байт
# Объекты класса <class 'list'> в количестве 1 заняли 88 байт
# Переменные заняли в сумме 280 байт
# Объекты класса <class 'int'> в количестве 5 заняли 140 байт


# вариант 3: с кортежем
# number = input('Введите целое положительное трехзначное число: ')
# tpl = tuple([int(i) for i in number])
# sum_digits = functools.reduce(lambda x, y: x + y, tpl)
# product_digits = functools.reduce(lambda x, y: x * y, tpl)
# print(f'Сумма равна {sum_digits}.'
#       f' Произведение равно {product_digits}.')
#
# sum_mem = SumMemory()
# sum_mem.extend(number, tpl, sum_digits, product_digits)
# print(sum_mem)
# Введите целое положительное трехзначное число: 345
# Объекты класса <class 'str'> в количестве 1 заняли 52 байт
# Переменные заняли в сумме 256 байт
# Объекты класса <class 'tuple'> в количестве 1 заняли 64 байт
# Переменные заняли в сумме 256 байт
# Объекты класса <class 'int'> в количестве 5 заняли 140 байт
