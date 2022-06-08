def leiaDinheiro(t):
    while True:
        print('-'*30)
        v = input(t)
        if v.find(',') >= 0:
            v = v.replace(',', '.')
        if v.find('.') >= 0:
            n = v.find('.' or ',')
            v1 = list(v)
            v1.pop(n)
            if ''.join(v1).isnumeric():
                break
        elif v.isnumeric():

            break
        print(f'ERRO: "{v}" é um preço inválido. Use apenas números e não utilize separador de milhar.')
    v = round(float(v), 2)
    return v
