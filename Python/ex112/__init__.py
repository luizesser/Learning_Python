from utilidadesCeV import moeda
from utilidadesCeV import dado

v = dado.leiaDinheiro('Digite um valor: R$')
moeda.resumo(v, 23, 7, dinheiro=True)
