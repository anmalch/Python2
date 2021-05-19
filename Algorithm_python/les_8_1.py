"""
Определение количества различных подстрок с использованием хэш-функции.
Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
Требуется найти количество различных подстрок в этой строке.
"""


def get_substrings(s):
    len_string = len(s)
    for len_substring in range(1, len_string):
        for i in range(len_string - len_substring + 1):
            yield s[i:i + len_substring]


st = set(get_substrings('abab'))

print(st)

print(f'Количество подстрок: {len(st)}')
