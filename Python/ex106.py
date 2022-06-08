def pyhelp():
    print('-'*30)
    print('Sistema de Ajuda PyHelp!')
    print('-'*30)
    print('Digite o nome de uma função ou biblioteca ou [fim] para sair.')
    i = str(input('Função ou Biblioteca > '))
    while i.strip().lower() != 'fim':
        print('~' * 30)
        print(f'Acessando o manual de {i}')
        print('~' * 30)
        help(i)
        print('-' * 30)
        i = str(input('Função ou Biblioteca > '))
    print('-' * 30)
    print('Obrigado por usar o PyHelp!')


pyhelp()
