# В заданном списке вещественных чисел найдите разницу между максимальным и
# минимальным значением дробной части элементов.
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import os
from random import *
os.system("cls")

list = [uniform(1, 21) for i in range(8)]
print(list)
list1 = []

for i in list:
    if i % 1 != 0:
        list1.append(i % 1)
print(list1)
print('Максимальное число: ', round(max(list1), 2))
print('Минимальное число: ', round(min(list1), 2))
print('Разница: ', round(max(list1) - min(list1), 2))
