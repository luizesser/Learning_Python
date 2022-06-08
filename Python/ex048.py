# soma entre todos os números impares, multiplos de três entre 1 e 500
s = 0
cont = 0
for c in range(0, 501, 3):
    if c % 2 == 1:
        cont += 1
        s += c
print('A soma de todos os números impares, multiplos de três entre 1 e 500 é {}'.format(s))
print('Foram encontrados um total de {} números.'.format(cont))
