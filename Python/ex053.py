from unidecode import unidecode
f = str(input('Digite uma frase para saber se ela é um palindromo: ')).strip()
f1 = ''.join(unidecode(f.lower()).split())
if f1 == f1[::-1]:
    print('A frase é um palindromo:\n{}\n{}'.format(f, f[::-1]))
else:
    print('A frase não é um palindromo:\n{}\n{}'.format(f, f[::-1]))
