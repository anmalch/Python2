"""
    Написать программу сложения и умножения двух шестнадцатеричных чисел.
    При этом каждое число представляется как массив, элементы которого это цифры числа.
    Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
    Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’]
"""
from collections import defaultdict

first_number = input('Введите первое число: ').upper()
second_number = input('Введите второе число: ').upper()


hex_elm = '0123456789ABCDEF'
hex_to_dec = defaultdict(int)
dec_to_hex = defaultdict(int)
i: int = 0
for key in hex_elm:
    hex_to_dec[key] += i
    i += 1
print(hex_to_dec)

for i in range(16):
    dec_to_hex[i] = hex_elm[i]
print(dec_to_hex)

first_list = []
second_list = []
rev_sum_list = []
mul_list = []

for elm in first_number:
    first_list.append(hex_to_dec[elm])

for elm in second_number:
    second_list.append(hex_to_dec[elm])

rev_first_list = list(reversed(first_list))
rev_second_list = list(reversed(second_list))

if len(rev_first_list) >= len(rev_second_list):
    longer_list = rev_first_list
    shorter_list = rev_second_list
else:
    longer_list = rev_second_list
    shorter_list = rev_first_list

addendum = 0

for i in range(len(shorter_list)):
    sum_ = shorter_list[i] + longer_list[i] + addendum

    addendum = 0

    if sum_ > 15:
        addendum = 1
        sum_ -= 16

    rev_sum_list.append(sum_)

if len(longer_list) > len(shorter_list):
    for i in range(len(shorter_list), len(longer_list)):
        sum_ = longer_list[i] + addendum

        addendum = 0

        if sum_ > 15:
            addendum = 1
            sum_ -= 16

        rev_sum_list.append(sum_)

if addendum > 0:
    rev_sum_list.append(addendum)

sum_list = list(reversed(rev_sum_list))

hex_sum_list = []
for elm in sum_list:
    hex_sum_list.append(dec_to_hex[elm])

print(hex_sum_list)