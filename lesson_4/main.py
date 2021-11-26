"""
#Задание №2.

print("Программа выводит элементы исходного списка, значения которых больше предыдущего элемента в списке.")

ishodni_spisok = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print("Исходный список:", ishodni_spisok)

new_spisok = [el1 for el1, el2 in zip(ishodni_spisok[1:], ishodni_spisok[:-1]) if el1 > el2]
print("Результат:", new_spisok)
"""
"""
#Задание №3.

print("Программа находит и выводит числа в пределах от 20 до 240, значения которых кратные 20 или 21.")

new_spisok_2 = [el for el in range(20, 241, 1) if el % 20 == 0 or el % 21 == 0]
print("Результат:", new_spisok_2)
"""
"""
#Задание №4.

print("Программа выводит элементы исходного списка, не имеющие повторений.")

ishodni_spisok_2 = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print("Исходный список:", ishodni_spisok_2)

new_spisok_3 = [el for el in ishodni_spisok_2 if ishodni_spisok_2.count(el) == 1]
print("Результат:", new_spisok_3)
"""
"""
#Задание №5.

print("Программа формирует список, в который входят четные числа от 100 до 1000 (включительно), и далее выводит результат вычисления произведения всех элементов списка.")

from functools import reduce
ishodni_spisok_3 = [el for el in range(100, 1001, 1) if el % 2 == 0]
print("Исходный список:", ishodni_spisok_3)
new_spisok_4_result = reduce(lambda x, y: x * y, ishodni_spisok_3)
print("Результат:", new_spisok_4_result)
"""
"""
# Задание №6.
# a)

from itertools import count

print("Программа генерирует 50 целых чисел, начиная с указанного вами.")

num = int(input("Введите любое целое число: "))
c = 0

for el in count(num + 1):
    if c > 49:
        break
    c += 1
    print("Результат №%s:" % c, el)
"""
"""
#б)

from itertools import cycle
print("Программа повторяет все элементы списка 2 раза.")
b = 0
ishodni_spisok_4 = [1, 2, 3, 4, "Пять"]
print("Исходный список значений:", ishodni_spisok_4)

for el in cycle(ishodni_spisok_4):
    if b > 9:
        break
    b += 1
    print("Результат №%s:" % b, el)
"""
"""
#Задание №7.

from itertools import count
from math import factorial
n = int(input("Введите любое целое неотрицательное число, чтобы получить его факториал: "))

def my_generator():
    for i in count(1):
        yield factorial(i)

my_g = my_generator()
x = 0
if n == 0:
    print("Вы ввели 0. Результат: 1.")
elif n < 0:
    print("Вы ввели отрицательное число.")
else:
    for k in my_g:
        if x < n:
            x += 1
            print("Результат №%s:" % x, k)
        else:
            break
"""
