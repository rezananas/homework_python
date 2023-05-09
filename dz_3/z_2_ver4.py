scrabble = [(1, 'AEIOULNSTRАВЕИНОРСТ'),                  # сделали из словаря список кортежей
            (2, 'DGДКЛМПУ'),
            (3, 'BCMPБГЁЬЯ'),
            (4, 'FHVWYЙЫ'),
            (5, 'KЖЗХЦЧ'),
            (8, 'JXШЭЮ'),
            (10, 'QZФЩЪ')]

my_dict = {}
[my_dict.update(my_dict.fromkeys(values, key)) for key, values in scrabble]
print(my_dict)

word = input('Введите слово: ')
total = 0

for letter in word.upper():
    total += my_dict.get(letter)

print(f'Слово "{word}" весит {total} баллов.')