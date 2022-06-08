def moeda(v=0, m='R$'):
    """
    Transforma um valor em monetário.
    :param m: padrão: R$.
    :param v: número float ou inteiro a ser transformado.
    :return: valor formatado.
    """
    v = str(v)
    return f'{m}{float(v):.2f}'


def aumentar(v=0, p=0, dinheiro=False):
    """
    Calcula o valor de um produto com aumento de p%.
    :param dinheiro: o retorno deve ser formatado como moeda? Booleano.
    :param v: valor (float) original do produto.
    :param p: porcentagem.
    :return: valor com o aumento.
    """
    v = float(v)
    p = float(p)
    r = v + (v * (p / 100))
    if dinheiro:
        return moeda(r)
    else:
        return r


def diminuir(v=0, p=0, dinheiro=False):
    """
    Calcula o valor de um produto com desconto de p%.
    :param dinheiro: o retorno deve ser formatado como moeda? Booleano.
    :param v: valor (float) original do produto.
    :param p: porcentagem.
    :return: valor com o desconto.
    """
    v = float(v)
    p = float(p)
    r = v - (v * (p / 100))
    if dinheiro:
        return moeda(r)
    else:
        return r


def metade(v=0, dinheiro=False):
    """
    Calcula a metade do valor dado.
    :param dinheiro: o retorno deve ser formatado como moeda? Booleano.
    :param v: valor.
    :return: a metade do valor.
    """
    v = float(v)
    r = v / 2
    if dinheiro:
        return moeda(r)
    else:
        return r


def dobro(v=0, dinheiro=False):
    """
    Calcula o dobro de um valor dado.
    :param dinheiro: o retorno deve ser formatado como moeda? Booleano.
    :param v: valor.
    :return: o dobro do valor.
    """
    v = float(v)
    r = v * 2
    if dinheiro:
        return moeda(r)
    else:
        return r

