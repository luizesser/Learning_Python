from math import radians, sin, cos, tan
n = float(input('Informe o valor do ângulo: '))
n2 = radians(n)
print('Para o ângulo de {} graus, ou {:.3f} radianos:\nSeno = {:.3f}\nCosseno = {:.3f}\nTangente = {:.3f}'
      .format(n, n2, sin(n2), cos(n2), tan(n2)))
