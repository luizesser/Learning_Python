v = float(input('Qual a velocidade do carro? '))
if v > 80:
    n = (v - 80) * 7
    print('Você foi multado em R${:.2f}.'.format(n))
print('Tenha um bom dia! Dirija com segurança!')
