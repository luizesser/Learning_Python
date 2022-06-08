cont = 'S'
c = 0
ls = []
print('=-'*30)
while cont == 'S':
    n = float(input('Digite um número: '))
    c += 1
    ls.append(n)
    cont = str(input('Deseja adicionar mais um número [S/N]? ')).strip().upper()[0]
    while cont not in 'SN':
        print('Código inválido, tente novamente. ', end='')
        cont = str(input('Deseja adicionar mais um número [S/N]? ')).strip().upper()[0]
print(f'Foram adicionados um total de {c} números.')
ls2 = ls[:]
ls2.sort(reverse=True)
print(f'A ordem decrescente dos valores é {ls2}.')
if 5 in ls:
    print(f'O número 5 faz parte da lista e sua primeira ocorrência é na posição {ls2.index(5)}.')
else:
    print('O número 5 não faz parte da lista.')
