
# #Задание №1.
#
# print("Программа создает тестовый файл my_file.txt и построчно записывает в него данные, которые ввёл пользователь.\n"
#       "Пустая строка означает конец ввода данных.")
#
# file = open("my_file.txt", 'w')
# file.close()
#
# with open("my_file.txt", 'a+', encoding='utf-8') as file:
#     data = ("")
#     while data != "\n":
#         file.write(data)
#         data = input("Введите любые данные для записи в файл my_file.txt: ") + "\n"
# print("Данные записаны.")
#
# #Задание №2.
#
# print("Программа считает количество строк и слов в файле, а также количество слов в каждой строке.")
#
# with open("new_file.txt", "r", encoding='utf-8') as file_2:
#     data = file_2.readlines()
#     print("Количество строк в файле:", len(data))
#     file_2.seek(0)
#     data = file_2.read()
#     words = data.split()
#     print('Количество слов в файле:', len(words))
#     file_2.seek(0)
#     num = 1
#     for line in file_2:
#         words = line.split()
#         print('Количество слов в строке №%s:' % num, len(words))
#         num += 1
#
# #Задание №3.
#
#
# with open("file_name.txt", "r", encoding='utf-8') as file_3:
#     data_2 = file_3.read().split("\n")
#     my_dict = dict()
#     for item in data_2:
#         key = item.split(" ")[0]
#         value = item.split(" ")[1]
#         my_dict[key] = value
#     print("Фамилии сотрудников, оклад которых менее 20000.")
#     salary = list(map(int, (my_dict.values())))
#     inv_my_dict = {value: key for key, value in my_dict.items()}
#     for i in salary:
#         if i < 20000:
#             i = str(i)
#             print(inv_my_dict[i], end='\n')
#     from statistics import mean
#     print("Средняя величина дохода сотрудников:", mean(salary))
#
#Задание №4.
#
# with open("new_file_2.txt", "r", encoding='utf-8') as file_4:
#     data_3 = file_4.readlines()
#     data_4 = []
#     rus = ["Один — 1", "Два — 2", "Три — 3", "Четыре — 4"]
#     eng = ["One — 1", "Two — 2", "Three — 3", "Four — 4"]
#     p = 0
#     for i in data_3:
#         data_4.append(i.replace(eng[p], rus[p]))
#         p += 1
#     with open('new_file_3.txt', 'w', encoding='utf-8') as file_5:
#         file_5.writelines(data_4)
#
# #Задание №5.
#
#
# with open('new_file_4.txt', 'w+') as file_6:
#     data_5 = input("Введите числа через пробел: ")
#     file_6.write(data_5)
#     file_6.seek(0)
#     data_6 = file_6.read().split()
#     result = [int(item) for item in data_6]
#     print(sum(result))
#
# #Задание №6.
#
# import re
#
# def calculate_hours(x):
#     line_of_hours = re.sub(r'\D', ' ', x)
#     ttl_hours = 0
#     for hour in line_of_hours.split():
#         ttl_hours += float(hour)
#     return ttl_hours
#
# overall_subject_info = {}
# with open('lessons.txt', 'r', encoding='utf-8') as file_7:
#     for line in file_7.readlines():
#         listed_line = line.split(': ')
#         overall_subject_info[listed_line[0]] = calculate_hours(listed_line[1])
#
# print(f'Результат:\n {overall_subject_info}')
#
# #Задание №7.
#
# import json
#
# result = []
# profit = {}
# average = []
#
# with open('task.txt', 'r', encoding='utf-8') as file_read:
#     counter = 1
#     while True:
#         line = file_read.readline().split()
#
#         if not line:
#             break
#
#         profit[line[0]] = float(line[-2]) - float(line[-1])
#
#         if profit[line[0]] > 0:
#             average.append(profit[line[0]])
#
#         counter += 1
#
#
# result = [profit, {'average_profit': sum(average) / len(average)}]
#
# with open('task.json', 'w', encoding='utf-8') as file_write:
#     json.dump(result, file_write)
