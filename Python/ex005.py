## Resolução:
# n = int(input('Digite um número:'))
# n1 = n + 1  # sucessor
# n2 = n - 1  # antecessor
# print('O número é {}. Seu sucessor é {}, e seu antecessor é {}.'.format(n, n1, n2))
## Alternativa usando menos memória:
n = int(input('Digite um número:'))
print('O número é {}. Seu sucessor é {} e seu antecessor é {}.'.format(n, n+1, n-1))
