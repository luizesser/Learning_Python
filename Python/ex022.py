nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...\nSeu nome em maiúsculas: {}\nSeu nome em minúsculas: {}\n'
      'Total de letras: {}\nLetras no primeiro nome: {}'
      .format(nome.upper(), nome.lower(), len(nome.replace(' ', '')), len(nome[:nome.find(' ')])))
