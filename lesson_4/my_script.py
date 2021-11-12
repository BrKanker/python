#Задание №1.

from sys import argv

script_name, first_param, second_param, third_param = argv

print("Имя скрипта: ", script_name)
print("Функция расчета заработной платы сотрудника.")
first_param = int(first_param)
second_param = int(second_param)
third_param = int(third_param)
print("Выработка в часах:", first_param)
print("Ставка в час:", second_param)
print("Премия:", third_param)

from my_functions import my_func

print("Заработная плата сотрудника: ", my_func(first_param, second_param, third_param))