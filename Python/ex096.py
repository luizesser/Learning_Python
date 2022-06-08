def area(l, c):
    a = l*c
    print(f'A área do terreno com {l}m de largura e {c}m de comprimento é de {a}m2.')


print('Controle de Terrenos')
print('-'*20)
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
area(largura, comprimento)
