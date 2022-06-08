nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
if media < 5:
    print('Média {}, menor do que 5. Reprovado.'.format(media))
elif media >= 7:
    print('Média {}, maior do que 7. Aprovado.'.format(media))
else:
    print('Média {}, entre 5 e 7. Recuperação.'.format(media))
