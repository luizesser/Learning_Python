from datetime import date
ano = int(input('Digite o ano de nascimento do atleta: '))
hoje = date.today().year
idade = hoje-ano
if idade <= 9:
    categoria = 'Mirim'
elif idade <= 14:
    categoria = 'Infantil'
elif idade <= 19:
    categoria = 'Júnior'
elif idade <= 25:
    categoria = 'Sênior'
else:
    categoria = 'Master'
print('Categoria: {}.'.format(categoria))
