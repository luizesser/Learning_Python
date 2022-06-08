def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        print(f'Com {idade} anos: VOTO NEGADO')
    elif 65 > idade > 18:
        print(f'Com {idade} anos: VOTO OBRIGATÓRIO')
    else:
        print(f'Com {idade} anos: VOTO OPCIONAL')


voto(int(input('Ano de nascimento: ')))
