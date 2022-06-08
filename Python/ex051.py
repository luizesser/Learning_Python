n = int(input('Digite o primeiro termo da Progressão Aritmética: '))
r = int(input('Digite a razão da Progressão Aritmética: '))
print('Os dez primeiros termos da PA são: ', end='')
for c in range(n, n+10*r, r):
    if c == n:
        print('{}'.format(c), end='')
    else:
        print(', {}'.format(c), end='')
print('.')
