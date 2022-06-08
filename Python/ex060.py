# Alternativa 0:
n = int(input('Digite um número para saber seu fatorial: '))
n2 = n
resultado = 1
f = []
while n > 0:
    resultado = resultado * n
    n -= 1
for i in range(n2, 0, -1):
    f += [i]
print('{}! = {} = {}'.format(n, f, resultado))

# Alternativa 1:
from math import factorial
n = int(input('Digite um número para saber seu fatorial: '))
f = factorial(n)
print('O fatorial de {} é {}.'.format(n, f))
# Alternativa 2:
n = int(input('Digite um número para saber seu fatorial: '))
n2 = n
resultado = 1
print('{}! = '.format(n), end='')
while n2 > 0:
    print('{}'.format(n2), end='')
    print(' x ' if n2 > 1 else ' = ', end='')
    resultado *= n2
    n2 -= 1
print('{}'.format(resultado))
# Alternativa 3 (usando for):
n = int(input('Digite um número para saber seu fatorial: '))
r = 1
print('{}! = '.format(n), end='')
for i in range(n, 0, -1):
    print('{}'.format(i), end='')
    print(' x ' if i > 1 else ' = ', end='')
    r *= i
print('{}'.format(r))
