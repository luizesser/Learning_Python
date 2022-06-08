m = float(input('Escreva um valor em metros:'))
print('Valor em milímetros: {}\nValor em centimetros: {}'.format(m*1000, m*100))
print('\nAlém disso, seus correspondentes em outras escalas são:\n'
      '{} km\n{} hm\n{} dam\n{} m\n{} dm\n{} cm\n{} mm'.format(m*0.001, m*0.01, m*0.1, m*1, m*10, m*100, m*1000))
