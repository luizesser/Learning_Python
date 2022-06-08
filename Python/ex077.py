vetor = 'praticar', 'comer', 'dancar', 'fazer'
vogais = 'a', 'e', 'i', 'o', 'u'
for p in vetor:
    #t = tuple(p)
    print(f'\nNa palavra {p} temos as vogais: ', end='')
    for v in p:
        if v in 'aeiou':
            print(f'{v} ', end='')
