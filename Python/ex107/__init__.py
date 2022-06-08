import moeda

v = float(input('Digite o preço do produto: R$'))
print(f'Se levar duas unidade paga R${moeda.dobro(v)}.')
print(f'Se levar metade de uma unidade paga R${moeda.metade(v)}')
print(f'Se pagar no débito ganha 10% de desconto. Paga R${moeda.diminuir(v, 10)}')
print(f'Se pagar no crédito paga 5% de juros. Paga R${moeda.aumentar(v, 5)}')
