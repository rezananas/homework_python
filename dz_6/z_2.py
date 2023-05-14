# Задача 32: Определить индексы элементов списка, значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума).

import random

minn = int(input("Введите минимальный элемент: "))
maxx = int(input("Введите максимальный элемент: "))

my_list = [random.randint(-10, 10) for _ in range(20)]
print(my_list)

for i in range(len(my_list)):
    if minn < my_list[i] < maxx:
        print(i, end=" ")