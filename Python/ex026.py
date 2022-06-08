frase = str(input('Digite uma frase: ')).strip().lower()
frase2 = frase.split('a')
#print('A frase possui {} letras A\nO primeiro A está na posição {}\nO último A está na posição {}'
#      .format(frase.count('a'), frase.find('a'), len(frase)-len(frase2[len(frase2)-1])-1))
## Alternativa melhor:
print('A frase possui {} letras A\nO primeiro A está na posição {}\nO último A está na posição {}'
      .format(frase.count('a'), frase.find('a'), frase.rfind('a')))
