n = int(input('Qual número você deseja saber a tabuada? '))
print('='*12)
print('TABUADA DO {}'.format(n))
print('='*12)
for c in range(1, 11):
    print('{} x {} = {}'.format(n, c, n*c))
print('='*12)
