maior = homens = mulher = 0
while True:
    print('-'*19)
    print('CADASTRE UMA PESSOA')
    print('-'*19)
    idade = str(input('Digite a idade: ')).strip()
    while not idade.isnumeric():
        idade = str(input('Digite a idade: ')).strip()
    else:
        idade = int(idade)
    sexo = str(input('Digite o sexo [M/F/X]: ')).strip().upper()[0]
    while sexo not in 'MFX':
        sexo = str(input('Digite o sexo [M/F/X]: ')).strip().upper()[0]
    if idade > 18:
        maior += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulher += 1
    print('-'*38)
    continuar = str(input('Deseja inserir mais uma pessoa [S/N]? ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Deseja inserir mais uma pessoa [S/N]? ')).strip().upper()[0]
    print('-'*38)
    if continuar == 'N':
        break
print(f'O número de pessoas maiores de 18 anos é {maior}.')
print(f'O número de homens é {homens}.')
print(f'O número de mulheres menores de 20 anos é {mulher}.')
print('-' * 15)
print('FIM DO PROGRAMA')
print('-' * 15)
