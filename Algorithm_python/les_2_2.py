"""
    Посчитать четные и нечетные цифры введенного натурального числа.
    Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5)

    https://drive.google.com/file/d/1-c9vOMQsLOY7X0w8UF7x7N5d7shKWT_h/view?usp=sharing
"""


def recursion(n):
    if n < 10:
        if n % 2 == 0:
            return 1
        else:
            return 0
    else:
        return recursion(n // 10) + recursion(n % 10)


number = int(input('Введите, пожалуста, натуральное число: '))
count = recursion(number)
print(f'Введенное число содержит {count} четных чисел и {len(str(number)) - count} нечетных чисел')
