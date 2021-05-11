'''
    Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

  В качестве переменных беру элементы типа int, list, tuple. Меньше памяти занимает переменная из первого варианта типа int,
  но это один объект , в отличии от списка и кортежа.
  Так как кортеж - это неизменяемый тип данных, ему не нужно резервировать память под дополнительные ячейки, поэтому он занимает
  меньше памяти, чем список.
'''
import functools
import sys


def show(obj) -> object:
    print(f'{type(obj)=}, {sys.getsizeof(obj)=}, {obj=}')
    if hasattr(obj, '__iter__'):
        if hasattr(obj, 'items'):
            for key, value in obj.items():
                show(key)
                show(value)
        else:
            for item in obj:
                show(item)


# вариант 1: 'переменная' - число
number = int(input('Введите целое положительное трехзначное число: '))

c = number % 10
b = number % 100 // 10
a = number // 100

sum_ = a + b + c
product_ = a * b * c
print(f'Сумма равна {sum_}.'
      f' Произведение равно {product_}.')

show(number)
# type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=345



# вариант 2: 'переменная' - список
#number = input('Введите целое положительное трехзначное число: ')
# lst = []
# for elm in number:
#     lst.append(int(elm))
#
# sum_ = functools.reduce(lambda x, y: x + y, lst)
# product_ = functools.reduce(lambda x, y: x * y, lst)
#
# show(lst)

# type(obj)=<class 'list'>, sys.getsizeof(obj)=88, obj=[3, 4, 5]
# type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=3
# type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=4
# type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=5



# вариант 3: 'переменная' - кортеж
# number = input('Введите целое положительное трехзначное число: ')
# tpl = tuple([int(i) for i in number])
# sum_ = functools.reduce(lambda x, y: x + y, tpl)
# product_ = functools.reduce(lambda x, y: x * y, tpl)
#
# show(tpl)

# type(obj)=<class 'tuple'>, sys.getsizeof(obj)=64, obj=(3, 4, 5)
# type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=3
# type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=4
# type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=5