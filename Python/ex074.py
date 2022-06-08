from random import randint
x = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Lista de números gerados: {x}.')
print(f'O maior número é {sorted(x)[-1]}.')
print(f'O menor número é {sorted(x)[0]}.')

# Alternativa:
num = x
print('Os números sorteados foram: ', end='')
for i in num:
    print(f'{i} ', end='')
print(f'\nO maior número é {max(num)}')
print(f'O menor número é {min(num)}')
