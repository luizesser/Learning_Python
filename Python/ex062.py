'''
n = int(input('Primeiro termo da PA: '))
n2 = n
r = int(input('Razão da PA: '))
m = 9
m2 = 1
while m2 != 0:
    n = n2
    m += m2
    pa = []
    max = n + m * r
    while n < max:
        pa += [n]
        n = n + r
    print('Os {} primeiros termos da PA são: {}.'.format(m, pa))
    m2 = int(input('Quantos termos a mais você deseja ver? '))
print('Fim do programa.')
'''
# Alternativa sem lista:
print('-='*20)
print('Gerador de PA')
print('-='*20)
n = int(input('Primeiro termo da PA: '))
r = int(input('Razão da PA: '))
print('-='*20)
n2 = n
print('Os dez primeiros termos da PA são: ', end='')
c = 1
mais = 1
total = 10
while mais != 0:
    while c <= total:
        print('{}'.format(n2), end='')
        print(' , ' if c < total else '.', end='')
        n2 += r
        c += 1
    mais = int(input('\nQuantos termos você quer mostrar a mais? '))
    total += mais
    if mais > 0:
        print('Os {} próximos termos da PA são: '.format(mais), end='')
print('Total de termos mostrados: {}.'.format(total))
print('\n')
print('-='*20)
