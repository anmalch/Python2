"""
     Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
     (т.е. 4 отдельных числа) для каждого предприятия..
     Программа должна определить среднюю прибыль (за год для всех предприятий)
     и вывести наименования предприятий, чья прибыль выше среднего и отдельно вывести наименования предприятий,
     чья прибыль ниже среднего.
"""
import collections

business_dict = collections.defaultdict(list)

#business_dict: dict[str, list] = {}

num = int(input("Введите количество предприятий: "))

for key in range(1, num + 1):
    business_name = input(f"Введите наименование предприятия: ")
    business_dict[business_name] = []

    for j in range(1, 5):
        profit = float(input(f"Введите прибыль за {j} квартал: "))
        business_dict[business_name].append(profit)

print(business_dict)

lst_profit = []
for value in business_dict.values():
    profit = sum(value)
    lst_profit.append(profit)

print(lst_profit)  # прибыль каждого за год

avg = sum(lst_profit) / len(lst_profit)

print("\nСредняя прибыль: %.3f. Предприятия с прибылью выше среднего:" % avg)
for key, value in business_dict.items():
    if avg < sum(value):
        print(key)

print("\nСредняя прибыль: %.3f. Предприятия с прибылью ниже среднего:" % avg)
for key, value in business_dict.items():
    if avg > sum(value):
        print(key)
