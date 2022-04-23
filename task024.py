# В заданном списке вещественных чисел найдите разницу между максимальным и
# минимальным значением дробной части элементов.
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import os
from random import *
os.system("cls")

list = [uniform(1, 21) for i in range(8)]
print(list, '\n')
for i in range(len(list)):
    list[i] = list[i] % 10/10
print(list)
print('\nМаксимальное число: ', max(list), '\n')
