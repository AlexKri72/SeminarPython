# Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
# Примеры
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"],
# ищем: "qwe", # ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"],
# ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"],
# ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"],
# ищем: "123", ответ: -1
# список: [],
# ищем: "123", ответ: -1

import os
os.system("cls")
list = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]
print(list)
str = input('Что будем искать?: ')
count = 0
for i in range(len(list)):
    if list[i] == str:
        count += 1
    if count == 2:
        print('Позиция второго вхождения равна ', i)
        break
if count != 2:
    print('-1')
