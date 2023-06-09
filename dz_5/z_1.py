# Задача 26:  Напишите программу, которая на вход принимает два числа A и B 
# и возводит число А в целую степень B с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8

num_a = int(input("Введите основание А: "))
num_b = int(input("Введите степень B: "))

def a_power_b(a, b):
    if b == 0:
        return 1
    return a * a_power_b(a, b-1)

print(f"Число {num_a} в степени {num_b} = {a_power_b(num_a, num_b)}")