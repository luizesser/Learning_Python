alt = float(input('Qual a altura da parede em metros?'))
lar = float(input('Qual a largura da parede em metros?'))
print('Para pintar uma parede de {} metros de altura por {} metros de largura, isto é, uma parede de {} m2, '
      'são necessários {} Litros de tinta.'.format(alt, lar, alt*lar, alt*lar/2))
