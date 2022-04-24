# Дана последовательность чисел. Получить список неповторяющихся элементов исходной последовательности
# Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [1, 2, 3, 5, 10]
import os
from random import*
os.system("cls")

# заполняем случайными числами исходный массив
list = [randint(1, 11) for i in range(1, 21)]
list1 = []
print(list)
for i in list:
    if list.count(i) == 1:  # выбираем неповторяющиеся числа
        list1.append(i)
print(list1)
