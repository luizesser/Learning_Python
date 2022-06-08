cont = 'S'
ls = []
print('-='*30)
while cont == 'S':
    n = int(input('Digite um valor: '))
    if ls.count(n) == 0:
        ls.append(n)
    else:
        print('Valores duplicados não serão adicionados...')
    cont = str(input('Deseja continuar [S/N]? ')).upper().strip()[0]
print('-=' * 30)
print(f'Você digitou os valores {sorted(ls)}.')
