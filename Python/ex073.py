t = ('Grêmio', 'Santos', 'Cruzeiro', 'Atlético Mineiro', 'Palmeiras', 'Botafogo', 'Flamengo',
     'Fluminense', 'Internacional', 'São Paulo', 'Corinthians', 'Chapecoense', 'Bahia',
     'Athletico Paranaense', 'Sport', 'Goiás', 'Coritiba', 'Vitória', 'Portuguesa', 'Náutico')
print('='*30)
print(f'Lista de times do Brasileirão: {t}')
print('-'*30)
print(f'Os 5 times do topo da tabela são: {t[:5]}')
print('-'*30)
print(f'Os 4 times da base da tabela são: {t[-4:]}')
print('-'*30)
print(f'A lista de times em ordem alfabética é: {sorted(t)}')
print('-'*30)
print(f'O time da Chapecoense está na {t.index("Chapecoense")+1}ª posição.')
print('='*30)
