# Tuplas:
# Vetores que aceitam misturar classes.
# Definidas por parêntesis ou não:
# loop com duas variáveis:
lanche = 'Hambúrger', 'Suco', 'Pizza', 'Pudim'
lanche = ('Hambúrger', 'Suco', 'Pizza', 'Pudim')

# utilizando em loop for:
for l1 in lanche:
    print(f'Vou comer um {l1}')

for n, l2 in enumerate(lanche):
    print(f'Vou comer um {l2} na posição {n}')

# TUPLAS SÃO IMUTÁVEIS.
# Mas dá pra mudar algumas coisas:
print(sorted(lanche))  # printa com [] pois vira lista.

# Com números agora:
a = 1, 2, 3, 5
b = 7, 6, 5
c = a + b
print(c)
c = b + a
print(c)
print(sorted(c))  # também printa com [], pois vira uma lista.
print(len(c))  # tamanho da tupla
print(c.count(5))  # quantas vezes aparece '5' na tupla?
texto = 'a', 'b', 'c', 'd', 'd', 'e'
print(texto.count('d'))  # serve para texto também.
print(c)
print(c.index(7))  # em que posição está o '7'?
print(c.index(5))  # tem dois '5', só o primeiro é retornado (posição 2), se eu quiser o próximo, então:
print(c.index(5, 3))  # isto é, o índice do '5', mas olhando apenas a partir da posição 3.

# Listas:
# São mutáveis.
# São marcadas por colchetes:
print(' LISTAS ')
x = ['a', 'b', 'c', 'd']  # Cria uma lista x, vazia.
print(x)
x[0] = 'y'  # altera o valor 0
print(x)
x.append('a')  # Adiciona um elemento no final da lista.
print(x)
x.insert(0, 'z')  # Adiciona 'z' em qualquer posição, empurrando os outros elementos pra frente.
print(x)
del x[3]  # deleta o elemento na posição 3.
print(x)
x.pop(3)  # deleta o elemento na posição 3. Se deixar os parêntesis vazios, elimina o último elemento.
print(x)
x.remove('a')  # deleta o primeiro elemento 'a'.
print(x)
# Criando listas:
valores = list(range(4, 11))  # cria números de 4 a 10.
print(valores)
valores = [4, 5, 6, 7, 8, 9, 10]  # cria a mesma lista.
print(valores)
valores = [8, 2, 5, 4, 9, 3, 0]  # cira uma lista com valores aleatórios e...
valores.sort(reverse=True)  # organiza os valores do maior para o menor.
print(valores)
print(len(valores))  # para saber o tamanho das listas, usa-se o len.
### DUPLICANDO ELEMENTOS !!! ###
# APENAS DECLARAR UMA IGUALDADE CRIA UM ELO ENTRE AS LISTAS E NÃO UM BACKUP!
# PARA DUPLICAR UMA LISTA:
a = [1, 2, 3, 4]
b = a
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
a = [1, 2, 3, 4]
b = a[:]  # b recebe todos os valores de a.
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')

## É possível usar listas dentro de listas:
galera = list()
dado = list()
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])  # Isso vai copiar os valores de dado para a lista galera.
    dado.clear()  # Limpa os valores dentro de dados
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
    if p[1] < 21:
        print(f'{p[0]} é menor de idade.')

### DICIONÁRIOS:
filme = {}
filme = dict()  # declara por chaves ou função dict.
filme = {
    'titulo': 'Star Wars',
    'ano': 1977,
    'diretor': 'George Lucas'
}
print(filme.values())  # 'Star Wars', 1977, George Lucas
print(filme.keys())  # titulo, ano, diretor
print(filme.items())  # retorna valores com as respectivas chaves.
for k, v in filme.items():  # k = keys, v = values
    print(f'O {k} é {v}. ', end='')  # O titulo é Star Wars. O ano é 1977. O diretor é George Lucas.
# pra incluir coisas:
filme['nota'] = 7  # automaticamente cria a key nota e inclui o value 7.
print(filme['nota'])
# pra copiar os dados, não dá pra usar [:], mas sim :
filme.copy()
del filme['titulo']  # deleta o título.
