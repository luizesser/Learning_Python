n = int(input('Quantos números da sequência de Fibonacci você deseja saber? '))
c = 1
f1 = 0
f2 = 1
r = [0, 1]
r2 = ['0', '1']
while c != n-1:
    f2 += f1
    r += [f2]
    f1 = r[c]
    c += 1
print('Os {} primeiros números da sequência de Fibonacci são:\n{}.'.format(n, r))
