lado1 = float(input('Digite o valor do primeiro lado do triângulo: '))
lado2 = float(input('Digite o valor do segundo lado do triângulo: '))
lado3 = float(input('Digite o valor do terceiro lado do triângulo: '))
if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    print('O triângulo é do tipo ', end='')
    if lado1 == lado2 == lado3:
        print('EQUILÁTERO.')
    elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
        print('ESCALENO.')
    else:
        print('ISÓSCELES')
else:
    print('Os lados não podem formar um triângulo.')
