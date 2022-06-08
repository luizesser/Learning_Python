'''n = int(input('Digite um ano: '))
if n % 400 == 0:
    print('{} é um ano bissexto, pois é divisível por 400.'.format(n))
else:
    if n % 100 == 0:
        print('{} não é um ano bissexto, pois não é divisível por 400 e é divisível por 100.'.format(n))
    else:
        if n % 4 == 0:
            print('{} é um ano bissexto, pois não é divisível por 400, nem por 100, mas é divisível por 4.'.format(n))
        else:
            print('{} não é um ano bissexto, pois não é divisível por 400, nem por 100, nem por 4.'.format(n))
 '''
# Alternativa usando 'and' e 'or':
from datetime import date
n = int(input('Qual ano você deseja analisar? Coloque 0 para alaisar o ano atual: '))
if n == 0:
    n = date.today().year
if n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
    print('O ano {} é bissexto.'.format(n))
else:
    print('O ano {} não é bissexto.'.format(n))
