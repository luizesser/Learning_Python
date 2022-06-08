from datetime import date
maior = 0
menor = 0
atual = date.today().year
for i in range(1, 8):
    ano = int(input('Digite o ano de nascimento da pessoa {}: '.format(i)))
    if atual - ano >= 21:
        maior += 1
    else:
        menor += 1
print('{} pessoas são maiores de idade (21 anos), enquanto {} pessoas são menores de idade.'
      .format(maior, menor))
