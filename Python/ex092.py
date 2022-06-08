from datetime import date
nome = str(input('Nome: ')).strip().title()
anon = int(input('Ano de nascimento: '))
ctps = int(input('Número da carteira de trabalho (0 se não tiver): '))
ano = date.today().year
idade = ano - anon
if ctps != 0:
    anoc = int(input('Ano de contratação: '))
    sal = float(input('Salário: R$'))
    aposentadoria = idade + (35 - (ano - anoc))
    pessoa = {'Nome': nome,
              'Idade': idade,
              'CTPS': ctps,
              'Ano de Contratação': anoc,
              'Salário': sal,
              'Idade da aposentadoria': aposentadoria}
else:
    pessoa = {'Nome': nome,
              'Idade': idade,
              'CTPS': ctps}
for k, v in pessoa.items():
    print(f'{k} tem o valor {v}.')
