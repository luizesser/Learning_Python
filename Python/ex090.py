aluno = dict()
aluno['Nome'] = str(input('Nome: ')).strip().title()
aluno['Nota'] = float(input('Média: '))
if aluno['Nota'] >= 7:
    aluno['Situação'] = 'Aprovado'
elif 5 <= aluno['Nota'] < 7:
    aluno['Situação'] = 'Recuperação'
else:
    aluno['Situação'] = 'Reprovado'
for k, v in aluno.items():
    print(f'{k} é {v}. ', end='')
