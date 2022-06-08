def fatorial(n, show=False):
    '''
    Calcula o fatorial de um dado número
    :param n: (Int) Número a ser calculado o fatorial.
    :param show: (Opcional/Boolean) Deseja mostrar o processo de cálculo? Padrão = False.
    :return: Se show=False, retorna o valor do fatorial (Int). Se show=True, retorna uma string com o processso.
    '''
    v = 1
    if show == True:
        print(f'{n}! = ', end='')
    for i in range(n, 0, -1):
        v *= i
        if show == True:
            if i != 1:
                print(f'{i} x ', end='')
            else:
                print(f'{i} = ', end='')
    print(f'{v}')
    return v


fatorial(5, show=True)
help(fatorial)
