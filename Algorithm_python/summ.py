"""
    Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах
"""
import sys


class SumMemory:
    def __init__(self):
        self._sum_memory = 0  # общее количество занятой памяти
        self._types = {}  # словарь вида {'type': [count, size]}

    def extend(self, *args): # проход по всем переменным
        for obj in args:
            self._add(obj)

    def _add(self, obj):
        spam = sys.getsizeof(obj)
        self._sum_memory += spam
        eggs = type(obj)
        if eggs in self._types:
            self._types[eggs][0] += 1
            self._types[eggs][1] += spam
        else:
            self._types[eggs] = [1, 1]
            self._types[eggs][1] = spam

        if hasattr(obj, '__iter__'):
            if hasattr(obj, 'items'):
                for key, value in obj.items():
                    self._add(key)
                    self._add(value)
            elif not isinstance(obj, str):
                for item in obj:
                    self._add(item)

    def __str__(self):
        return f'\nПеременные заняли в сумме {self._sum_memory} байт' \
               f'\n'.join([f'Объекты класса {key} '
                           f'в количестве {value[0]} '
                           f'заняли {value[1]} байт'
                           for key, value in self._types.items()])
