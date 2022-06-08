print('='*18)
print('LEITOR DE PRODUTOS')
print('='*18)
total = caro = q = precobarato = 0
while True:
    q += 1
    nome = str(input('NOME DO PRODUTO: ')).strip()
    preco = str(input('PREÇO: R$')).strip()
    while not preco.replace('.', '').isnumeric():
        print('Preço inválido. Digite apenas números.')
        preco = str(input('PREÇO: R$')).strip()
    preco = float(preco)
    total += preco
    if preco > 1000:
        caro += 1
    if q == 1 or precobarato >= preco:
        precobarato = preco
        nomebarato = nome
    c = str(input('Deseja adicionar mais algum produto [S/N]? ')).strip().upper()[0]
    if c not in 'SN':
        print('Código inválido.')
        c = str(input('Deseja adicionar mais algum produto [S/N]? ')).strip().upper()[0]
    print('='*18)
    if c == 'N':
        break
print(f'Você inseriu {q} produto(s).\n'
      f'O total gasto na compra foi de R${total:.2f}.\n'
      f'Sendo {caro} produto(s) com o valor maior que R$ 1000,00.\n'
      f'O produto mais barato foi: {nomebarato}. Seu preço é de R${precobarato:.2f}.')
print('='*18)
