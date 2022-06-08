print('-='*30)
print('Calculadora limitada!')
print('-='*30)
print('Digite os dois valores que deseja trabalhar.')
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
m = 0
while m != 5:
    print('Os valores são {} e {}.'.format(n1, n2))
    m = int(input('''   O que deseja fazer com esses valores?
    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] SABER QUAL O MAIOR
    [ 4 ] DIGITAR NOVOS NÚMEROS
    [ 5 ] SAIR
    Digite uma opção:  '''))
    if m == 1:
        print('\nA soma dos dois números é {}.\n'.format(n1+n2))
    elif m == 2:
        print('\nO produto dos dois números é {}.\n'.format(n1*n2))
    elif m == 3:
        print('\nO maior valor digitado é {}.\n'.format(n1) if n1 > n2
              else '\nO maior valor digitado é {}\n'.format(n2))
    elif m == 4:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
print('-='*30)
print('Calculadora encerrada.')
print('-='*30)