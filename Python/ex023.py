n = str(int(input('Digite um número entre 0 e 9999: ')))
n2 = int(4-len(n))
n3 = n2*'0'+n
print('Unidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}'
      .format(n3[3], n3[2], n3[1], n3[0]))

### ALTERNATIVA:
#num = int(input('Informe um número: '))
#u = num // 1 % 10
#d = num // 10 % 10
#c = num // 100 % 10
#m = num // 1000 % 10
#print('Unidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}'
#      .format(u, d, c, m))