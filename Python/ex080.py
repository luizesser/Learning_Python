'''
ls = []
print('-='*30)
for i in range(0, 5):
    n = float(input('Digite um número: '))
    if i == 0:
        ls.append(n)
        print(f'{n} adicionado na posição 0.')
    else:
        for c in range(0, len(ls)):
            if ls[c] >= n:
                ls.insert(c, n)
                print(f'{n} adicionado na posição {c}.')
                break
            elif c == len(ls)-1:
                ls.append(n)
                print(f'{n} adicionado no final da lista.')
                break
print('-='*30)
print(f'Os números digitados em ordem foram: {ls}.')
'''
#### Alternativa unindo os dois append:
ls = []
print('-='*30)
for i in range(0, 5):
    n = float(input('Digite um número: '))
    if i == 0 or n > ls[-1]:
        ls.append(n)
        print(f'{n} adicionado no final da lista.')
    else:
        for c in range(0, len(ls)):
            if ls[c] >= n:
                ls.insert(c, n)
                print(f'{n} adicionado na posição {c}.')
                break
print('-='*30)
print(f'Os números digitados em ordem foram: {ls}.')
