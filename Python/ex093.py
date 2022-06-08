nome = str(input('Nome do jogador: ')).strip().title()
njogos = int(input('Número de jogos jogados: '))
gols = list()
for c in range(0, njogos):
    gols.append(int(input(f'Número de gols na {c+1}a partida: ')))
total = sum(gols[:])
d = {'Nome': nome, 'Gols': gols[:], 'Total': total}
for k, v in d.items():
    print(f'O campo {k} tem valor {v}.')
print(f'O jogador {nome} jogou {len(d["Gols"])} partidas.')
for c in range(0, njogos):
    print(f'No {c+1}o jogo marcou {d["Gols"][c]} gols.')
print(f'Foi um total de {total} gols.')
