from utilidadesCeV import moeda

v = input('Qual o valor a ser sumarizado: ')
a = input('Qual a porcentagem a ser acrescida: ')
d = input('Qual a porcentagem a ser diminuida: ')

moeda.resumo(v, a, d, dinheiro=True)
