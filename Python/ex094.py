pessoas = list()
while True:
    nome = str(input('Nome: ')).strip().title()
    sexo = str(input('Sexo [M/F/X]: ')).strip().upper()[0]
    idade = int(input('Idade: '))
    cont = str(input('Deseja incluir mais uma pessoa [S/N]? ')).strip().upper()[0]
    p = {'Nome': nome, 'Sexo': sexo, 'Idade': idade}
    pessoas.append(p.copy())
    if cont == 'N':
        break
print(pessoas)
print(f'Foram cadastradas {len(pessoas)} pessoas.')
media = sum(d['Idade'] for d in pessoas)/len(pessoas)
print(f'A média de idade é {media} anos.')
mulheres = sum(d['Sexo'] == 'F' for d in pessoas)
print(f'O número de mulheres cadastradas foi {mulheres}.')
acima = sum(d['Idade'] > media for d in pessoas)
print(f'{acima} pessoas tem idade acima da média.')
print('São elas:')
for d in pessoas:
    if d['Idade'] > media:
        print(f'Nome = {d["Nome"]}; ', end='')
        print(f'Sexo = {d["Sexo"]}; ', end='')
        print(f'Idade = {d["Idade"]}.')
