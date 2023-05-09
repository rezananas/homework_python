scrabble = {'AEIOULNSTRАВЕИНОРСТ' : 1,
            'DGДКЛМПУ' : 2,
            'BCMPБГЁЬЯ' : 3,
            'FHVWYЙЫ' : 4,
            'KЖЗХЦЧ' : 5,
            'JXШЭЮ' : 8,
            'QZФЩЪ' : 10}

word = input('Введите слово: ')
total = 0

for letter in word.upper():
    for letters in scrabble.keys():
        if letter in letters:
            total += scrabble.get(letters)
            break

print(f'Слово "{word}" весит {total} баллов.')