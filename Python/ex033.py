'''n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
n = [n1, n2, n3]
n.sort()
print('O maior número é {}, enquanto o menor é {}'.format(n[2], n[0]))
'''
# Alternativa:
a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
c = int(input('Digite mais um número: '))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O maior número inserido foi {}\nO menor número inserido foi {}'.format(maior, menor))
