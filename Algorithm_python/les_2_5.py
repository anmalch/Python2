"""
    В программе генерируется случайное целое число от 0 до 100.
    Пользователь должен его отгадать не более чем за 10 попыток.
    После каждой неудачной попытки должно сообщаться больше или меньше введенное пользователем число,
    чем то, что загадано. Если за 10 попыток число не отгадано, то вывести загаданное число.

    https://drive.google.com/file/d/1g1ADEqnfLf1R8lQlpQlxGpDLgQMZB8JP/view?usp=sharing
"""

import random

number = random.randint(0, 101)


count = 0
while count <= 10:
    user_number = int(input('Введите, пожалуйста, число: '))
    count += 1
    if user_number == number:
        print(f'Поздравляем! Вы угадали число {number} за {count} попыток')
        break
    else:
        if user_number < number:
            print(f'Попробуйте снова. Подсказка: загаданное число больше {user_number}')
        else:
            print(f'Попробуйте снова. Подсказка: загаданное число меньше {user_number}')

else:
    print('Не расстраивайтесь. Не везет в игре, повезет в любви!')
