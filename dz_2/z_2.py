# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
# Пример:
# 4 4 -> 2 2
# 5 6 -> 2 3

summ = int(input("Введите сумму натуральных чисел: "))
mult = int(input("Введите произведение натуральных чисел: "))

if summ > 0 and mult > 0:
    for i in range(summ):
        for j in range(mult):
            if i + j == summ and i * j == mult:
                print(f"Задуманные числа: {i} {j}")
else:
    print("Нет таких натуральных чисел")