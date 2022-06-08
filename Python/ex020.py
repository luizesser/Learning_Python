#from random import sample
#n1 = input('Nome do primeiro aluno: ')
#n2 = input('Nome do segundo aluno: ')
#n3 = input('Nome do terceiro aluno: ')
#n4 = input('Nome do quarto aluno: ')
#n = (n1, n2, n3, n4)
#resultado = sample(n, 4)
#print('A ordem de apresentação será:\n1. {}\n2. {}\n3. {}\n4. {}'
#      .format(resultado[0], resultado[1], resultado[2], resultado[3]))

### ALTERNATIVA
from random import shuffle
n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem de apresentação será:\n{}'.format(lista))
