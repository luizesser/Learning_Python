x = int(input('Digite um número: ')), int(input('Digite um número: ')), \
    int(input('Digite um número: ')), int(input('Digite um número: '))
print('A sequência de números digitada foi: ', end='')
for i in x:
    print(f'{i}', end=' ')
n9 = x.count(9)
if n9 >= 2:
    print(f'\nO número 9 apareceu {n9} vezes.')
elif n9 == 1:
    print(f'\nO número 9 apareceu {n9} vez.')
elif n9 == 0:
    print(f'\nO número 9 não apareceu nenhuma vez.')
if x.count(3) > 0:
    print(f'O número 3 aparece pela primeira vez na posição {x.index(3)+1}.')
else:
    print(f'O número 3 não foi digitado.')
c = 0
for i in x:
    if i % 2 == 0:
        c += 1
if c >= 2:
    print(f'Foram digitados {c} números pares.')
elif c == 1:
    print(f'Foi digitado {c} número par.')
elif c == 0:
    print('Nenhum número par foi digitado.')
