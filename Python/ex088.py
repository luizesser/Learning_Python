from random import randint
from time import sleep
print('=-'*20)
print('{:^40}'.format('Gerador de palpites - MEGASENA'))
print('=-'*20)
p = int(input('Quantos palpites você quer gerar? '))
print('{:^40}'.format(f' < SORTEANDO {p} JOGOS > '))
pal = list()
res = list()
for j in range(0, p):
    for i in range(0, 6):
        n = randint(1, 60)
        while n in pal:
            n = randint(1, 60)
        pal.append(n)
    pal.sort()
    res.append(pal[:])
    pal.clear()
for j in range(1, p+1):
    print(f'Jogo {j}: {res[j-1]}')
    sleep(0.5)
print('{:^40}'.format(f' < BOA SORTE! > '))
