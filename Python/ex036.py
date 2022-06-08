casa = float(input('Valor do imóvel: R$'))
salario = float(input('Salário do comprador: R$'))
anos = float(input('Prazo em anos para quitar o imóvel: '))
prestacao = casa/(anos * 12)
if prestacao > 0.3 * salario:
    print('O empréstimo foi negado, pois o valor da prestação (R${:.2f}) '
          'é maior que 30% do valor do salário (R${:.2f}).'.format(prestacao, salario))
else:
    print('O empréstimo foi aprovado, pois o valor da prestação (R${:.2f}) '
          'é menor que 30% do valor do salário (R${:.2f}).'.format(prestacao, salario))
