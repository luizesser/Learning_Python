# ESTRUTURAS DE CONTROLE:
# 1. CONDICIONANTES ANINHADOS
'''nome = str(input('Qual é o seu nome? '))
if nome == 'Luiz':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'João':  # else+if = elif (dá pra inserir quantos elif quiser...)
    print('Seu nome é bem popular no Brasil.')
elif nome == 'Vunibaldo':
    print('Meu avô também se chama Vunibaldo!')
elif nome in 'Ana Cláudia Jéssica Paula':
    print('Belo nome feminino.')
else:  # usa só uma vez (por último), ou não usa.
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(nome))
#
#
# 2. Laços de Repetição (estrutura de repetição com variável de controle)
for c in range(0, 6):  # Repete o conteúdo do laço 6 vezes: 0, 1, 2, 3, 4, 5
    print('Oi')
print('FIM')
# outra ideia:
for c in range(1, 6):  # printa uma contagem de 1 a 5
    print(c)
print('FIM')
# contando de trás pra frente:
for c in range(5, 0, -1):  # começa no 5, tira 1, 4, tira 1, 3, -1, 2, -1, 1. (último número -zero- não conta).
    print(c)
print('FIM')
# Contar números:
n = 10
for c in range(1, n+1):
    print(c)
# alternativa:
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('FIM')
# somando números:
s=0
for c in range(0, 4):
    n = int(input('Digite um número: '))
    s += n  # Uma alternativa equivalente é:  s = s + n
print('Total = {}'.format(s))
'''
#loop com duas variáveis:
lanche = 'Hambúrger', 'Suco', 'Pizza', 'Pudim'
for n, l in enumerate(lanche):
    print(f'Vou comer um {l} na posição {n}')
'''
# estrutura de repetição com teste lógico (while)
# para interromper o laço:
n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break# interrompe o laço.
    s += n
print(f'A soma é {s}.')
'''