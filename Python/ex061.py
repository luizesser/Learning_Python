'''
# Gerador de PA usando lista
print('-='*20)
print('Gerador de PA')
print('-='*20)
n = int(input('Primeiro termo da PA: '))
r = int(input('Razão da PA: '))
print('-='*20)
max = n+10*r
pa = []
while n < max:
    pa += [n]
    n = n+r
print('Os dez primeiros termos da PA são: {}.'.format(pa))
print('-='*20)
'''
# sem usar lista:
print('-='*20)
print('Gerador de PA')
print('-='*20)
n = int(input('Primeiro termo da PA: '))
r = int(input('Razão da PA: '))
print('-='*20)
n2 = n
print('Os dez primeiros termos da PA são: ', end='')
c = 1
while c <= 10:
    print('{}'.format(n2), end='')
    print(' , ' if c < 10 else '.', end='')
    n2 += r
    c += 1
print('\n')
print('-='*20)
