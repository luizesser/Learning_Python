import moeda

v = float(input('Digite o preço do produto: R$'))
print(f'Se levar duas unidade paga {moeda.dobro(v, dinheiro=True)}.')
print(f'Se levar metade de uma unidade paga {moeda.metade(v, dinheiro=True)}')
print(f'Se pagar no débito ganha 10% de desconto. Paga {moeda.diminuir(v, 10, dinheiro=True)}')
print(f'Se pagar no crédito paga 5% de juros. Paga {moeda.aumentar(v, 5, dinheiro=True)}')
