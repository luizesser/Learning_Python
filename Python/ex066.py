c = soma = n = 0
while True:
    c = int(input('Digite um valor para somar (999 para encerrar): '))
    if c == 999:
        break
    soma += c
    n += 1
print(f'A soma dos {n} valores digitados é {soma}.')
