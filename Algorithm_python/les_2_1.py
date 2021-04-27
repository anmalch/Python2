"""
    Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
    Числа и знак операции вводятся пользователем. После выполнения вычисления программа не должна завершаться,
    а должна запрашивать новые данные для вычислений.
    Завершение программы должно выполняться при вводе символа '0' в качестве знака операции.
    Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке
    и снова запрашивать знак операции. Также сообщать пользователю о невозможности деления на ноль,
    если он ввел 0 в качестве делителя.
    https://drive.google.com/file/d/1Q4IpthnE2hPBDAWraigqbWdajyG7PVdU/view?usp=sharing

"""
operation = None

while operation != '0':
    operation = None
    number1 = int(input('Введите первое число: '))
    number2 = int(input('Введите второе число: '))
    while operation not in ('+', '-', '*', '/', '0'):
        operation = input('Введите знак арифметической операции (сложение, вычитание, умножение или деление): ')
        if operation not in ('+', '-', '*', '/', '0'):
            print('Вы ввели не верный знак операции.')
    if operation == '+':
        print(number1 + number2)
    elif operation == '-':
        print(number1 - number2)
    elif operation == '*':
        print(number1 * number2)
    elif operation == '/':
        if number2 == 0:
            print('Деление на ноль')
        else:
            print(number1 / number2)



