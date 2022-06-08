c = 'Pão', 5.99, 'Leite', 3.50, 'Água', 1.00, 'Computador', 1000, 'Tv', 2345.99
print('-'*40)
print('{: ^40}'.format('LISTA DE COMPRAS'))
print('-'*40)
for i in range(0, len(c), 2):
    print('{:.<30}'.format(c[i]), end='')
    print('R$ ', end='')
    print('{: >7.2f}'.format(c[i+1]))
print('-'*40)
# Alternativa:
for i in range(0, len(c), 2): print(f'{c[i]:.<30}R$ {c[i+1]:>7.2f}')
