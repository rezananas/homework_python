# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X.
# 16. *Пример:*
# 5
#     1 2 3 4 5
#     3
#     -> 1
# 18. *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5

import random

size = int(input("Введите размер списка: "))
min_limit = int(input("Введите минимальный предел: "))
max_limit = int(input("Введите максимальный предел: "))

my_list = [random.randint(min_limit, max_limit) for _ in range(size)]
print(my_list)
number = int(input("Введите искомое число: "))

count = my_list.count(number)

closest = my_list[0]
if count == 0:
    for item in my_list:
        if abs(number - item) < abs(number - closest):
            closest = item

print(f"Число {number} встречается {count} раз." if count > 0 else f"Ближайшее к {number} число: {closest}.")