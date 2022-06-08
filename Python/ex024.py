nome = str(input('Digite o nome da cidade: ')).strip()
print('A cidade {}, começa com a palavra "Santo"? {}'.format(nome, nome[:5].lower() == 'santo'))
