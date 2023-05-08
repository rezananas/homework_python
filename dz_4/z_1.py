# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. 
# n — кол-во элементов первого множества. 
# m — кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

from random import randint

num_1 = int(input("Введите количество элементов первого множества: "))
num_2 = int(input("Введите количество элементов второго множества: "))

list_1 = []
for i in range(num_1):
    list_1.append(randint(1,10))
set_1 = set(list_1)
print(set_1)

list_2 = []
for i in range(num_2):
    list_2.append(randint(1,10))
set_2 = set(list_2)
print(set_2)

set_all = set_1 & set_2
print(set_all)

list_all = list(set_all)
list_all.sort()
print(list_all)