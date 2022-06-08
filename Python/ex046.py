from time import sleep
print('='*41)
print('O foguete vai ser lançado em 10 segundos!')
print('='*41)
for c in range(10, -1, -1):
    print('#####\n# {} #\n#####'.format(c))
    sleep(1)
print('='*7)
print('Lançar!')
print('='*7)
