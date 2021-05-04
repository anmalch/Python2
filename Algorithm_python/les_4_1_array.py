"""
    В массиве случайных целых чисел поменять местами минимальный и максимальный элементы

"""

import cProfile
import random


def swap_min_max_1(array):
    if len(array) == 0:
        return array

    min_ = array[0]
    min_index = 0
    for i in range(len(array)):
        if array[i] < min_:
            min_ = array[i]
            min_index = i

    max_ = array[0]
    max_index = 0
    for i in range(len(array)):
        if array[i] > max_:
            max_ = array[i]
            max_index = i

    array[min_index], array[max_index] = array[max_index], array[min_index]
    return array


def swap_min_max_2(array):
    if len(array) == 0:
        return array

    min_index = array.index(min(array))
    max_index = array.index(max(array))

    array[min_index], array[max_index] = array[max_index], array[min_index]
    return array


def test_swap_1(func):
    given_array = [1, 2]

    actual_array = func(given_array)

    assert actual_array == [2, 1], f'Ошибка в test_swap_1'
    print(f'Тест test_swap_1 прошел успешно')


def test_swap_2(func):
    given_array = [1, 2, 3, 4, 5, 99]

    actual_array = func(given_array)

    assert actual_array == [99, 2, 3, 4, 5, 1], f'Ошибка в test_swap_2'
    print(f'test_swap_2 прошел успешно')


def test_swap_empty(func):
    given_array = []

    actual_array = func(given_array)

    assert actual_array == [], f'test_swap_empty'
    print(f'Тест test_swap_empty прошел успешно')


# test_swap_empty(swap_min_max_1)
# test_swap_empty(swap_min_max_2)

# test_swap_2(swap_min_max_1)
# test_swap_2(swap_min_max_2)

# test_swap_1(swap_min_max_1)
# test_swap_1(swap_min_max_2)


def main1(n):
    MIN_ITEM = 0
    MAX_ITEM = 100
    return swap_min_max_1([random.randint(MIN_ITEM, MAX_ITEM) for _ in range(n)])


def main2(n):
    MIN_ITEM = 0
    MAX_ITEM = 100
    return swap_min_max_2([random.randint(MIN_ITEM, MAX_ITEM) for _ in range(n)])


"""
print(timeit.timeit('main1(10)', number=100, globals=globals()))       # 0.0030595999999999957
print(timeit.timeit('main1(50)', number=100, globals=globals()))       # 0.012863883000000007
print(timeit.timeit('main1(500)', number=100, globals=globals()))      # 0.138411097
print(timeit.timeit('main1(5000)', number=100, globals=globals()))     # 0.9113547850000001
print(timeit.timeit('main1(100_000)', number=100, globals=globals()))  # 14.918021747000001

"""
"""
print(timeit.timeit('main2(10)', number=100, globals=globals()))       # 0.003011398999999998
print(timeit.timeit('main2(50)', number=100, globals=globals()))       # 0.008919598
print(timeit.timeit('main2(500)', number=100, globals=globals()))      # 0.13202423400000002
print(timeit.timeit('main2(5000)', number=100, globals=globals()))     # 0.926758326
print(timeit.timeit('main2(100_000)', number=100, globals=globals()))  # 13.691935961

"""
# При использовании встроенных функций поиска минимального и максимального значений в массиве программа работает немного быстрее,
# чем при использовании циклов, особенно это стало заметно на большом массиве, но не критично, я считаю.
# cProfile.run('main1(100_000)')
# Здесь я наблюдаю, что самая затратная функция randrange(). А также написанная мною функция с циклами гораздо медленее,
# чем со встроенными функциями нахождения минимума и максимума
"""
 ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.271    0.271 <string>:1(<module>)
        1    0.015    0.015    0.015    0.015 les_4_1_array.py:11(swap_min_max_1)
        1    0.000    0.000    0.271    0.271 les_4_1_array.py:81(main1)
        1    0.039    0.039    0.256    0.256 les_4_1_array.py:84(<listcomp>)
   100000    0.065    0.000    0.093    0.000 random.py:237(_randbelow_with_getrandbits)
   100000    0.080    0.000    0.173    0.000 random.py:290(randrange)
   100000    0.044    0.000    0.217    0.000 random.py:334(randint)
        1    0.000    0.000    0.271    0.271 {built-in method builtins.exec}
        3    0.000    0.000    0.000    0.000 {built-in method builtins.len}
   100000    0.011    0.000    0.011    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
   126532    0.016    0.000    0.016    0.000 {method 'getrandbits' of '_random.Random' objects}

"""
cProfile.run('main2(100_000)')
# Здесь я наблюдаю, что самая затратная функция randrange(),
# а также что количество вызовов метода '_random.Random' гораздо больше 100_000.
# Сравнимая функции swap_min_max_1 и swap_min_max_2 по параметру cumtime, делаю вывод,
# что функция с циклами работате в 4 раза медленее, чем со встроенными функциями.
"""
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.335    0.335 <string>:1(<module>)
        1    0.000    0.000    0.004    0.004 les_4_1_array.py:33(swap_min_max_2)
        1    0.000    0.000    0.335    0.335 les_4_1_array.py:87(main2)
        1    0.055    0.055    0.331    0.331 les_4_1_array.py:90(<listcomp>)
   100000    0.082    0.000    0.117    0.000 random.py:237(_randbelow_with_getrandbits)
   100000    0.104    0.000    0.222    0.000 random.py:290(randrange)
   100000    0.055    0.000    0.276    0.000 random.py:334(randint)
        1    0.000    0.000    0.335    0.335 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.002    0.002    0.002    0.002 {built-in method builtins.max}
        1    0.002    0.002    0.002    0.002 {built-in method builtins.min}
   100000    0.014    0.000    0.014    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
   126824    0.021    0.000    0.021    0.000 {method 'getrandbits' of '_random.Random' objects}
        2    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}
   
"""
