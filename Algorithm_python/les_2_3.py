"""
    Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
    Количество элементов (n) вводится с клавиатуры

    https://drive.google.com/file/d/1U4lRt2UQgRZPRQC1cZ7j3xECTmrr1ISB/view?usp=sharing
"""
num = int(input('Введите, пожалуста, число: '))


def rec(z, n):
    if n == 1:
        return z
    else:
        return z + rec(z * (-0.5), n - 1)


sum = rec(1, num)
print(sum)
