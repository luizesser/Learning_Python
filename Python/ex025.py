nome = str(input('Digite seu nome completo: ')).strip()
nome = nome.title()
if nome.find('Silva') > 0:
    res = 'Sim'
else:
    res = 'Não'
print('O nome {} contém o sobrenome "Silva"? {}'.format(nome, res))
