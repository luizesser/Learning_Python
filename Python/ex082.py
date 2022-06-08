cont = 'S'
ls = []
while cont == 'S':
    n = int(input('Digite um número: '))
    ls.append(n)
    cont = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
pares = []
impares = []
for i in ls:
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)
print(f'A lista digitada foi: {ls}')
print(f'Os valores pares digitados são: {pares}')
print(f'Os valores impares digitados são: {impares}')
