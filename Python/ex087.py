matriz = [[], [], []]
somapar = soma3 = maior2 = 0
for i in range(0, 3):
    for j in range(0, 3):
        n = int(input(f'Digite um número para [{i}, {j}]: '))
        matriz[i].append(n)
        if n % 2 == 0:
            somapar += n
        if j == 2:
            soma3 += n
print('='*30)
print('A matriz completa é:')
for i in range(0, 3):
    for j in range(0, 3):
        print(f'[ {matriz[i][j]:^5} ]', end='')
    print()
print(f'A soma de todos os valores pares da matriz é {somapar}.')
print(f'A soma dos valores da terceira coluna da matriz é {soma3}.')
print(f'O maior valor da segunda linha da matriz é {max(matriz[1])}.')
