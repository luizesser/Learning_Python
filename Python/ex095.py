jogadores = list()
while True:
    print('-'*40)
    nome = str(input('Nome do jogador: ')).strip().title()
    njogos = int(input('Número de jogos jogados: '))
    gols = list()
    for c in range(0, njogos):
        gols.append(int(input(f'Número de gols na {c+1}a partida: ')))
    total = sum(gols)
    d = {'Nome': nome, 'Gols': gols, 'Total': total}
    jogadores.append(d.copy())
    cont = str(input('Adicionar mais jogadores [S/N]? ')).strip().upper()[0]
    if cont == 'N':
        break
print('-='*25)
print('{:<3}'.format('ID'), end='')
print('{:20}'.format('NOME'), end='')
print('{:<20}'.format('GOLS'), end='')
print('{:>6}'.format('TOTAL'))
print('-='*25)
for i in range(0, len(jogadores)):
    d = jogadores[i]
    print('{:<3}'.format(i), end='')
    print('{:20}'.format(d['Nome']), end='')
    print('{:<20}'.format(str(d['Gols'])), end='')
    print('{:>6}'.format(d['Total']))
print('-' * 50)
while True:
    c = int(input('Mostrar dados de qual jogador? (digite 999 para sair) iD: '))
    if c == 999:
        break
    d = jogadores[c]
    print(f'Dados do jogador {d["Nome"]}:')
    for c in range(0, len(d['Gols'])):
        print(f'No {c + 1}o jogo marcou {d["Gols"][c]} gols.')
    print('-'*50)
print('Finalizando...')
print('<<< Volte Sempre! >>>')
