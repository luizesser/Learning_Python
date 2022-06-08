'''
print('='*40)
print('{:^40}'.format('CAIXA ELETRÔNICO'))
print('='*40)
valor = str(input('Notas de 50, 20, 10 e 1 real.\nDigite o valor a ser sacado: R$')).strip()
while not valor.isnumeric():
    print('Valor indisponível.')
    valor = str(input('Notas de 50, 20, 10 e 1 real.\nDigite o valor a ser sacado: R$')).strip()
print('='*40)
valor = int(valor)
valor2 = valor
n50 = valor2//50
valor2 -= 50*n50
n20 = valor2//20
valor2 -= 20*n20
n10 = valor2//10
valor2 -= 10*n10
n1 = valor2//1
valor2 -= 1*n1
print(f'Sacando o valor de R${valor}.')
print(f'Total de cédulas de R$50: {n50}')
print(f'Total de cédulas de R$20: {n20}')
print(f'Total de cédulas de R$10: {n10}')
print(f'Total de cédulas de R$1: {n1}')
print('='*40)
print('Tenha um bom dia!')
'''
# Alternativa com while:
print('='*40)
print('{:^40}'.format('CAIXA ELETRÔNICO'))
print('='*40)
valor = str(input('Notas de 50, 20, 10 e 1 real.\nDigite o valor a ser sacado: R$')).strip()
while not valor.isnumeric():
    print('Valor indisponível.')
    valor = str(input('Notas de 50, 20, 10 e 1 real.\nDigite o valor a ser sacado: R$')).strip()
print('='*40)
valor = int(valor)
ced = 50
nced = 0
while True:
    if valor >= ced:
        valor -= ced
        nced += 1
    else:
        if nced > 0:
            print(f'{nced} cédulas de R${ced}.')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        nced = 0
        if valor == 0:
            break
print('=' * 40)
print('Tenha um bom dia!')
