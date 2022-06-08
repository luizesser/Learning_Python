dados = list()
nomes = list()
notas = list()
n1 = list()
n2 = list()
print('-='*20)
print('{:^40}'.format(' BOLETIM DE CLASSE '))
print('-='*20)
while True:
    nome = str(input('Nome do aluno: ')).strip().title()
    nomes.append(nome)
    nota1 = float(input('Primeira Nota: '))
    n1.append(nota1)
    nota2 = float(input('Segunda Nota: '))
    n2.append(nota2)
    c = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    if c == 'N':
        break
notas.append(n1[:])
notas.append(n2[:])
dados.append(nomes[:])
dados.append(notas[:])
print('-='*20)
print('{:<5}'.format('No.'), end='')
print('{:29}'.format('NOME'), end='')
print('{:>6}'.format('MÉDIA'))
print('-'*40)
for a in range(0, len(dados[0])):
    print('{:<5}'.format(a), end='')
    print('{:29}'.format(dados[0][a]), end='')
    m1 = float(dados[1][0][a])
    m2 = float(dados[1][1][a])
    m = (m1+m2)/2
    print('{:>6.2f}'.format(m))
print('-'*40)
while True:
    c = str(input('Mostrar notas de qual aluno (digite 0 para sair)? ')).strip().title()
    if c == '0':
        break
    no = dados[0].index(c)
    print(f'As notas de {c} foram: {dados[1][0][no]} e {dados[1][1][no]}.')
    print('-'*40)
print('Finalizando...')
print('<<< Volte Sempre! >>>')
### Uma alternativa seria fazer uma lista com 3 posições: nome, notas (n1 e n2), média.
