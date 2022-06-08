from random import randint


def sorteia(n):
    s = []
    for i in range(0, n):
        rand = randint(1, 10)
        s.append(rand)
    return s


def somapar(lst):
    soma = 0
    for i in range(0, len(lst)):
        if lst[i] % 2 == 0:
            soma += lst[i]
    return soma


ns = sorteia(5)
print(f'Os valores sorteados foram {ns}.')
print(f'A soma dos valores pares é {somapar(ns)}.')
ns = sorteia(10)
print(f'Os valores sorteados foram {ns}.')
print(f'A soma dos valores pares é {somapar(ns)}.')
ns = sorteia(3)
print(f'Os valores sorteados foram {ns}.')
print(f'A soma dos valores pares é {somapar(ns)}.')
