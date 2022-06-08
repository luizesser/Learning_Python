while True:
    print('-='*30)
    n = int(input('Digite um número para calcular sua tabuada\nou um número negativo para sair: '))
    if n < 0:
        break
    print('-='*30)
    print(f'A tabuada de {n} é:')
    print('-='*30)
    for i in range(1, 11):
        print(f'{n} x {i} = {n*i}')
print('-='*30)
print('Programa encerrado.')
