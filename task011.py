# Сформировать список из N членов последовательности.
# Для N = 5:         1, -3, 9, -27, 81 и т.д.
import os
os.system("cls")

n = int(input('Введите количество элементов последовательности: '))
list = []
for i in range(n):
    if i % 2 == 0:
        list.append(3**i)
    else:
        list.append(-3**i)
print(list, '\n')
