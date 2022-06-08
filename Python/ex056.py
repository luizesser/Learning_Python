'''import pandas as pd
nm = []
id = []
sx = []
for i in range(1, 5):
    print('-='*17)
    print('Dados da pessoa {}'.format(i))
    print('-='*17)
    nome = str(input('Primeiro Nome: ')).strip().title()
    nm += [nome]
    idade = int(input('Idade: '))
    id += [idade]
    sexo = str(input('Sexo (M/F/X): ')).strip().upper()
    sx+= [sexo]
print('-='*17)
d = {'nome': nm, 'idade': id, 'sexo': sx}
df = pd.DataFrame(data=d)
print(df)
print('-='*17)
print('RESULTADOS')
print('-='*17)
print('A média de idade do grupo é de {:.1f}'.format(df['idade'].mean()))
df2 = df[df['sexo'] == 'F']
df2 = df2[df2['idade'] < 20]
print('{} pessoas do sexo feminino possuem menos de 20 anos.'.format(len(df2.index)))
df2 = df[df['sexo'] == 'M']
idmax = df2['idade'].max()
df2 = df[df['idade'] == idmax]
print('O nome da pessoa mais velha e do sexo masculino é {}, com {} anos de idade.'.format(df2.iat[0,0], idmax))
print('-='*17)
'''
### ALTERNATIVA:
somaidade = 0
maioridadehomem = 0
nomevelho = ''
nmulheres = 0
for p in range(1, 5):
    print('----- {}a Pessoa -----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F/X]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        nmulheres += 1
mediaidade = somaidade / 4
print('-'*30)
print('A média de idade do grupo é de {} anos.'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maioridadehomem, nomevelho))
print('O número de mulheres menores de 20 anos é {}.'.format(nmulheres))

