# Найти сумму чисел списка стоящих на нечетной позиции
import os
from random import *
os.system("cls")

list = [randint(1, 21) for i in range(7)]
print(list, '\n')
sum = 0
for i in range(0, len(list), 2):
    sum += list[i]
print('Сумма элементов на нечетных позициях равна ', sum, '\n')
