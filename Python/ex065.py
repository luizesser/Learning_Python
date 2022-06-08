n = []
c = 'S'
while c == 'S':
    n1 = int(input('Digite um número: '))
    n += [n1]
    c = str(input('Deseja continuar inserindo números [s/n]? ')).strip().upper()[0]
tamanho = len(n)
media = sum(n) / tamanho
n.sort()
print('Você inseriu {} números. São eles:\n'
      '{}\n'
      'O menor número foi {}.\n'
      'O maior número foi {}.\n'
      'A média entre os valores é {}.'
      .format(len(n), n, n[0], n[tamanho-1], media))
