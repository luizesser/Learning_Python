'''n = float(input('Qual o salário do funcionário? R$'))
if n > 1250:
    print('O funcionário receberá um aumento de R${:.2f}, o equivalente a 10% de aumento.\n'
          'O novo salário é de R${:.2f}.'.format(n*0.1, n*1.1))
else:
    print('O funcionário receberá um aumento de R${:.2f}, o equivalente a 15% de aumento\n'
          'O novo salário é de R${:.2f}.'.format(n*0.15, n*1.15))
'''
# Alternativa:
n = float(input('Qual o salário atual do funcionário? '))
print('O novo salário é de R${}'.format(n*1.1) if n > 1250
      else 'O novo salário é de R${}'.format(n*1.15))
