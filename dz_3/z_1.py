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

my_list = [random.randint(0,10) for _ in range(size)]
print(my_list)

num = int(input("Введите искомое число: "))
count = 0
min_abs = 10

for i in range(size):
    if my_list[i] == num:
        count += 1
    else:
        num_abs = abs(my_list[i]-num)
        if num_abs < min_abs:
            min_abs = num_abs
            index = i

print(f"Число {num} встречается {count} раз. Ближайшее к нему число = {my_list[index]}.")