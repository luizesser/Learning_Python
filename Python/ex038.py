n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
if n1 > n2:
    print('{} é o maior número.'.format(n1))
elif n2 > n1:
    print(('{} é o maior número'.format(n2)))
else:
    print('Os números tem o mesmo tamanho.')
