p = []
for i in range(1, 6):
    peso = float(input('Digite o peso da pessoa {}: '.format(i)))
    p += [peso]
p.sort()
print('A pessoa com menor peso, possui {}Kg, enquanto a pessoa com maior peso possui {}Kg'
      .format(p[0], p[len(p)-1]))
