my_dict = {}
my_dict.update(my_dict.fromkeys('AEIOULNSTRАВЕИНОРСТ', 1))
my_dict.update(my_dict.fromkeys('DGДКЛМПУ', 2))
my_dict.update(my_dict.fromkeys('BCMPБГЁЬЯ', 3))
my_dict.update(my_dict.fromkeys('FHVWYЙЫ', 4))
my_dict.update(my_dict.fromkeys('KЖЗХЦЧ', 5))
my_dict.update(my_dict.fromkeys('JXШЭЮ', 8))
my_dict.update(my_dict.fromkeys('QZФЩЪ', 10))
print(my_dict)

word = input('Введите слово: ')
total = 0

for letter in word.upper():
    total += my_dict.get(letter)

print(f'Слово "{word}" весит {total} баллов.')