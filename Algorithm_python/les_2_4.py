"""
    Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
    Например, если введено число 3486, то надо вывести число 6843.
    https://drive.google.com/file/d/1wNQJJTZBEA7ne2rfDzKKfOl-Qj1Yhb4D/view?usp=sharing
"""
user_number = int(input('Введите, пожалуйста, число: '))

#print(int(''.join(reversed(user_number)))) как быстрый вариант

reverse_number = 0

while user_number > 0:
    rest = user_number % 10
    user_number = user_number // 10
    reverse_number = reverse_number * 10
    reverse_number = reverse_number + rest

print(reverse_number)