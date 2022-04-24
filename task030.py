# Вычислить число π c заданной точностью d Пример: при d = 0.001,π = 3.141.
# 10^(-1)  ≤  d  ≤  10^(-10)  (до 10 знаков после запятой)

import os
from math import pi
from random import*
os.system("cls")

a = randint(1, 10)
print('Точность вывода = ', a)

print('Пи = ', round(pi, a), '\n')
