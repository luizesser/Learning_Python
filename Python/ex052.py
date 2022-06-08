n = int(input('Digite um número para saber se ele é primo: '))
p = 'S'
m = []
for c in range(2, n, 1):
    if n % c == 0:
        p = 'N'
        m += [c]
if p == 'S':
    print('O número {} é primo'.format(n))
else:
    print('O número {} não é primo, pois é múltiplo de:\n{}'.format(n, m))
