'''
    Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.
    Начало
    Ввод letter1, letter2
    определить место первой буквы в алфавите
    определить место второй буквы в алфавите
    определить сколько между ними находится букв (letters)
    Вывод letter1, letter2
    Конец

   https://drive.google.com/file/d/1ROyJaX8P3aOjNas7_l5bYmE4P05NyIlV/view?usp=sharing
'''


letter1 = input('Введите первую букву: ')
letter2 = input('Введите вторую букву: ')

index_a = ord('a')
index1 = ord(letter1) - index_a + 1
index2 = ord(letter2) - index_a + 1

letters = abs(index2 - index1) - 1


print(f'Буква {letter1} стоит на {index1} месте латинского алфавита, а буква {letter2} - на {index2}, между ними находится {letters} букв.')

