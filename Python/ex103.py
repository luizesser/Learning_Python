def ficha(nome, gols):
    if nome == '':
        nome = '<desconhecido>'
    if not gols.isnumeric():
        gols = 0
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


n = str(input('Nome do Jogador: ')).strip().title()
g = input('Gols feitos: ')
ficha(nome=n, gols=g)
