from random import sample
from time import sleep
print('-='*10)
print('Vamos jogar Jokenpô?')
print('-='*10)
player = str(input('Pedra, papel ou tesoura?\nQual a sua escolha? ')).strip().upper()
print('-='*10)
sleep(0.5)
print('JO', end='')
sleep(0.5)
print('KEN', end='')
sleep(0.5)
print('PO!!!')
sleep(0.5)
print('-='*10)
opcoes = ['PEDRA', 'PAPEL', 'TESOURA']
if player not in opcoes:
    player = 'uma jogada inválida'
computador = str(sample(opcoes, 1)[0])
if computador == player:
    print('Computador escolheu {}.\nJogador escolheu {}.\nO jogo empatou!'.format(computador, player))
else:
    if player == 'PEDRA' and computador == 'TESOURA':
        vencedor = 'jogador'
    elif player == 'PAPEL' and computador == 'PEDRA':
        vencedor = 'jogador'
    elif player == 'TESOURA' and computador == 'PAPEL':
        vencedor = 'jogador'
    else:
        vencedor = 'computador'
    print('Computador escolheu {}.\nJogador escolheu {}.\nO vencedor foi o {}!'.format(computador, player, vencedor))
print('-='*10)
