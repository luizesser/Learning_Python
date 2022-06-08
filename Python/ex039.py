from datetime import date
nascimento = int(input('Qual o ano de nascimento do jovem? '))
ano = date.today().year
idade = ano-nascimento
print('Quem nasceu em {} tem {} anos de idade.'.format(nascimento, idade))
if idade < 18:
    print('Ainda faltam {} anos para você se alistar no serviço militar.\n'
          'Você deve se alistar no ano de {}.'.format(18-idade, nascimento+18))
elif idade > 18:
    print('Já passaram {} anos desde que você se alistou no serviço militar.\n'
          'O ano do seu alistamento foi {}.'.format(idade-18, nascimento+18))
else:
    print('Está na hora de você se alistar no serviço militar.')
