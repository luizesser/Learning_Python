print('-='*20)
print('{: ^40}'.format(' LOJAS TANIJO '))
print('-='*20)
preco = float(input('TOTAL DAS COMPRAS: R$'))
forma = int(input('Formas de pagamento:\n'
                  '[1] À vista dinheiro/cheque (10% de desconto)\n'
                  '[2] À vista no cartão (5% de desconto)\n'
                  '[3] Parcelado\n'
                  'Digite o código da forma escolhida: '))
if forma == 3:
    vezes = int(input('Condições:\n'
                      'Até 2x: sem juros.\n'
                      'Mais de 2x: 20% de juros.\n'
                      'Número de parcelas: '))
    if vezes > 2:
        total = preco*1.2
    else:
        total = preco
elif forma == 2:
    vezes = 1
    total = preco*0.95
elif forma == 1:
    vezes = 1
    total = preco*0.9
else:
    vezes = 'XXX'
    total = 'XXX'
    print('Código Inválido.')
print('Total a pagar: R${:.2f}.'.format(total))
print('Sua compra será parcelada em {}x de R${:.2f} com juros.'.format(vezes, total/vezes) if forma == 3 else '')
