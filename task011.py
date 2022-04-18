# Сформировать список из N членов последовательности.
# Для N = 5:         1, -3, 9, -27, 81 и т.д.
import os
os.system("cls")

n = int(input('Введите количество элементов последовательности: '))
for i in range(n):
    if i % 2 == 0:
        print(3**i, end=' ')
    else:
        print(-1 * 3**i, end=' ')
print('\n')
