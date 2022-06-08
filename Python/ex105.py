def notas(*n, sit=False):
    """Função para analisar as notas e situações dos alunos.
    :param n: (Int) as notas dos alunos.
    :param sit: (opcional/booleano) situação dos alunos.
    :return: um dicionário com a quantidade de notas insetidas, a maior e menor nota, a média e (opcional) a situação.
    """
    q = len(n)
    maior = max(n)
    menor = min(n)
    media = sum(n)/q
    d = {'Quantidade de Notas': q, 'Maior nota': maior, 'Menor nota': menor, 'Média': media}
    if sit:
        d2 = list()
        for i in range(0, q):
            if n[i] >= 7:
                d2.append('APROVADO')
            elif n[i] < 5:
                d2.append('REPROVADO')
            else:
                d2.append('RECUPERAÇÃO')
        d['Situação'] = d2
    return d


print(notas(3, 5, 7.5, 9, 10, sit=True))
