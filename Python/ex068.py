from random import randint
print('-='*30)
print('VAMOS JOGAR PAR OU IMPAR!')
print('-='*30)
c = 0
while True:
    e = str(input('Você escolhe PAR ou IMPAR [P/I]? ')).strip().upper()[0]
    while e not in 'PpIi':
        print('Escolha inválida.')
        e = str(input('Você escolhe PAR ou IMPAR [P/I]? ')).strip().upper()[0]
    n1 = str(input('Digite um número: ')).strip()
    while not n1.isnumeric():
        print('Informação inválida.')
        n1 = str(input('Digite um número: ')).strip()
    n1 = int(n1)
    n2 = randint(1, 2)
    print('-' * 60)
    print(f'Você escolheu {n1} e o computador escolheu {n2}.')
    if (n1+n2) % 2 > 0:
        r = 'IMPAR'
        f = 'I'
    else:
        r = 'PAR'
        f = 'P'
    print(f'A soma dos dois é {n1+n2}, um valor {r}.')
    if f == e:
        print('Você venceu!')
        print('Vamos jogar novamente...')
        print('-=' * 30)
        c += 1
    else:
        break
print('-='*30)
print(f'Você perdeu!\nVitórias consecutivas: {c}')
