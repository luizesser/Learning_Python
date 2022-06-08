'''
from random import randint
from time import sleep
jogo = {
    'jogador1': randint(1, 6),
    'jogador2': randint(1, 6),
    'jogador3': randint(1, 6),
    'jogador4': randint(1, 6)
}
for k, v in jogo.items():
    sleep(0.5)
    print(f'O {k} tirou {v}.')
print('=-'*30)
resultado = sorted(jogo.items(), key=lambda x: x[1], reverse=True)
for i in range(0, len(resultado)):
    sleep(0.5)
    print(f'O {resultado[i][0]} ficou em  {i+1}o lugar com o valor {resultado[i][1]}.')
'''
### Alternativa:
from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
for k, v in jogo.items():
    sleep(0.5)
    print(f'O {k} tirou o valor {v}.')
print('-='*30)
resultado = sorted(jogo.items(), key=itemgetter(1), reverse=True)  # itemgetter = 0 chave; = 1 valor. Output é lista.
for i, v in enumerate(resultado):
    sleep(0.5)
    print(f'{i+1}o Lugar: {v[0]} que tirou {v[1]}.')
