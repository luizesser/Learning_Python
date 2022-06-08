n = soma = 0
while n != 999:
    n = int(input('Digite um número inteiro para somar [999 para parar]: '))
    if n != 999:
        soma += n
print('A soma dos valores digitados é {}.'.format(soma))
