dados = list()
nomep = list()
nomel = list()
count = pesado = leve = 0
while True:
    count += 1
    dados.append(str(input('Digite o nome da pessoa: ')))
    dados.append(float(input('Digite o peso da pessoa (Kg): ')))
    if count == 1:
        pesado = leve = dados[1]
        nomep.append(dados[0])
        nomel.append(dados[0])
    else:
        if dados[1] > pesado:
            pesado = dados[1]
            nomep.clear()
            nomep.append(dados[0])
        elif dados[1] == pesado:
            nomep.append(dados[0])
        elif dados[1] < leve:
            leve = dados[1]
            nomel.clear()
            nomel.append(dados[0])
        elif dados[1] == leve:
            nomel.append(dados[0])
    dados.clear()
    cont = str(input('Deseja adicionar mais uma pessoa[S/N]? ')).strip().upper()[0]
    if cont == 'N':
        break
print(f'Você entrou os dados de {count} pessoas.')
print(f'O menor peso é {leve}, que é o peso de {nomel}.')
print(f'O maior peso é {pesado}, que é o peso de {nomep}.')
