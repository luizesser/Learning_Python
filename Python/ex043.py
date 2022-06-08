altura = float(input('Digite a altura da pessoa em centimetros: '))
peso = float(input('Digite o peso da pessoa em kilos: '))
imc = peso / (altura*0.01)**2
if imc < 18.5:
    print('Abaixo do peso.\nIMC = {:.1f}'.format(imc))
elif imc < 25:
    print('Peso ideal.\nIMC = {:.1f}'.format(imc))
elif imc < 30:
    print('Acima do peso.\nIMC = {:.1f}'.format(imc))
elif imc < 40:
    print('Obesidade.\nIMC = {:.1f}'.format(imc))
else:
    print('Obesidade mórbida.\nIMC = {:.1f}'.format(imc))
