n = int(input('Qual número você deseja converter? '))
base = int(input('Qual a base de conversão?\n'
                 'Digite 1 para binário.\n'
                 'Digite 2 para octal.\n'
                 'Digite 3 para hexadecimal.\n'
                 'Digite o código, conforme instrução acima: '))
if base == 1:
    nb = bin(n)
    print('Número em binário: {}'.format(nb.replace('0b', '')))
elif base == 2:
    no = oct(n)
    print('Número em octal: {}'.format(no.replace('0o', '')))
elif base == 3:
    nx = hex(n)
    print('Número em hexadecimal: {}'.format(nx.replace('0x', '')))
else:
    print('Código inválido.')
# também podia ter sido feito usando nb[2:] (mais fácil).
