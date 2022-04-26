# Строка содержит набор чисел. Показать большее и меньшее число Символ-разделитель - пробел

import os
os.system("cls")

str = '443 43245 5675 889 8789725 1235 4957 4627'
print(str)

str = str.split()
str = list(map(int, str))
print(str)

print('\nМаксимальное число: ', max(str))
print('Минимальное число: ', min(str), '\n')
