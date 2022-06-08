dias = int(input('Por quantos dias o carro foi alugado?'))
km = float(input('Quantos Km foram rodados?'))
print('O total a pagar é de R${:.2f}.'.format((60*dias)+(0.15*km)))
