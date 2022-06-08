print('-='*20)
print('Analisador de Triângulos')
print('-='*20)
a = float(input('Tamanho reta 1: '))
b = float(input('Tamanho reta 2: '))
c = float(input('Tamanho reta 3: '))
if a + b > c and b + c > a and a + c > b:
    print('As retas podem formar um triângulo.')
else:
    print('As retas não podem formar um triângulo.')
