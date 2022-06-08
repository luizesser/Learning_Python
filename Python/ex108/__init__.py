import moeda

v = float(input('Digite o preço do produto: R$'))
print(f'Se levar duas unidade paga {moeda.moeda(moeda.dobro(v))}.')
print(f'Se levar metade de uma unidade paga {moeda.moeda(moeda.metade(v))}')
print(f'Se pagar no débito ganha 10% de desconto. Paga {moeda.moeda(moeda.diminuir(v, 10))}')
print(f'Se pagar no crédito paga 5% de juros. Paga {moeda.moeda(moeda.aumentar(v, 5))}')
