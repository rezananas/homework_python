scrabble = [(1, 'AEIOULNSTRАВЕИНОРСТ'),
            (2, 'DGДКЛМПУ'),
            (3, 'BCMPБГЁЬЯ'),
            (4, 'FHVWYЙЫ'),
            (5, 'KЖЗХЦЧ'),
            (8, 'JXШЭЮ'),
            (10, 'QZФЩЪ')]

my_dict = {}
[my_dict.update(my_dict.fromkeys(values, key)) for key, values in scrabble]
word = input('Введите слово: ').upper()
total = sum([my_dict.get(letter) for letter in word])
print(f'Слово "{word}" весит {total} баллов.')