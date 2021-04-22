'''
     Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого)
     Начало
     Ввод a, b, c
     if a > b,
       if a > c,
          if b > c, then a>b>c
          else a>c>b
       else c>a>b
     elif  c > b, then c>b>a
     else
       if a > c, then b>a>c
       else b>c>a

    https://drive.google.com/file/d/1lGQj09bvKTfpOSWPjNBfqANxYhbeyNYR/view?usp=sharing
'''

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))

if a > b:
    if a > c:
        if b > c:
            print(f'{b} - среднее число, оно меньше {a}, но больше {c}.')
        else:
            print(f'{c} - среднее число, оно меньше {a}, но больше {b}.')
    else:
        print(f'{a} - среднее число, оно меньше {c}, но больше {b}.')

elif c > b:
        print(f'{b} - среднее число, оно меньше {c}, но больше {a}.')

else:
    if a > c:
        print(f'{a} - среднее число, оно меньше {b}, но больше {c}.')
    else:
        print(f'{c} - среднее число, оно меньше {b}, но больше {a}.')