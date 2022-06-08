n = int(input('Quantos kilômetros você vai percorrer?'))
if n <= 200:
    preco = 0.5*n
    print('O preço total da passagem é de R${}.'.format(preco))
else:
    preco = 0.45*n
    print('O preço total da passagem é de R${}.'.format(preco))
# preco = n * 0.5 if n <= 200 else n * 0.45
