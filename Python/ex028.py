from random import randint
from time import sleep
n = randint(0, 5)
print('-='*30)
print('Vou pensar em um némero entre 0 e 5. Tente adivinhar...')
print('-='*30)
n2 = int(input('Em que número eu pensei? '))
print('Processando...')
sleep(2)
print('Parabéns, você ganhou! O número era {}'.format(n) if n == n2 else 'Você perdeu... O número era {}!'.format(n))
