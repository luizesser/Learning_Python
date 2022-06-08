#import math
#ca = float(input('Valor do cateto adjacente = '))
#co = float(input('Valor do cateto adjacente = '))
#print('A hipotenusa é igual a {:.2f}'.format(math.sqrt((ca ** 2 + co ** 2))))
### Alternativa:
from math import hypot
ca = float(input('Valor do cateto adjacente = '))
co = float(input('Valor do cateto oposto = '))
print('A hipotenusa é igual a {:.2f}'.format(hypot(co, ca)))
