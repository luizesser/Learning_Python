from random import randint
computador = randint(1, 10)
jogador = 0
print('-='*30)
print('Pensei em um número entre 1 e 10.\n'
      'Quantas tentativas você precisa\n'
      'para adivinhar o número?')
print('-='*30)
c = 0
while jogador != computador:
    jogador = int(input('Que número você acha que eu pensei? '))
    c += 1
    if jogador == computador:
        print('Parabéns! Você acertou em {} tentativas!'.format(c))
    elif jogador > computador:
        print('Eu não escolhi o número {}. Tente um número menor...'.format(jogador))
    elif jogador < computador:
        print('Eu não escolhi o número {}. Tente um número maior...'.format(jogador))
