s = 'A'
while s not in 'FfMm':
    s = input('Sexo [M/F]: ')
    if s not in 'FfMm':
        print('Código inválido, tente novamente.')
    else:
        if s in 'Mm':
            s = 'masculino'
        else:
            s = 'feminino'
        print('O sexo escolhido foi o {}.'.format(s))
        s='f'
print('FIM')
