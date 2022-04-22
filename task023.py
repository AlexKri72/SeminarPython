# Найти произведение пар чисел в списке.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15]

import os
from random import *
os.system("cls")

list = [randint(1, 21) for i in range(8)]
print(list, '\n')
for i in range(int(len(list)/2)):
    print(list[i] + list[len(list)-1-i], end='      ')
