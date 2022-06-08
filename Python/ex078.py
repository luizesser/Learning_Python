l = []
for i in range(0, 5):
    l.append(input(f'Digite um número para a posição {i}: '))
print('-='*30)
print(f'Você digitou os valores {l}.')
print(f'O maior número digitado foi {max(l)}, nas posições ', end='')
for c, i in enumerate(l):
    if i == max(l):
        print(f'{c} ', end='')
print(f'\nO menor número digitado foi {min(l)}, nas posições ', end='')
for c, i in enumerate(l):
    if i == min(l):
        print(f'{c} ', end='')
