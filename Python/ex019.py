#from random import randint
#nome1 = input('Nome do primeiro aluno: ')
#nome2 = input('Nome do segundo aluno: ')
#nome3 = input('Nome do terceiro aluno: ')
#nome4 = input('Nome do quarto aluno: ')
#lista = (nome1, nome2, nome3, nome4)
#escolhido = randint(1, 4)
#print('O alunx escolhidx foi: {}'.format(lista[escolhido]))
### ALTERNATIVA:
from random import choice
n1 = input('1o Aluno: ')
n2 = input('2o Aluno: ')
n3 = input('3o Aluno: ')
n4 = input('4o Aluno: ')
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print('O alunx escolhidx foi {}.'.format(escolhido))
