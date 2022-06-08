from time import sleep


def lin():
    print('-'*30)


def contador(inicio, fim, passo):
    if inicio < fim:
        if passo == 0:
            passo = 1
        print(f'Contagem de {inicio} até {fim} de {passo} em {passo}: ')
        while inicio <= fim:
            sleep(0.5)
            print(inicio, end=' ')
            inicio += passo
    elif fim < inicio:
        if passo == 0:
            passo = -1
        if passo > 0:
            passo *= -1
        print(f'Contagem de {inicio} até {fim} de {passo} em {passo}: ')
        while inicio >= fim:
            sleep(0.5)
            print(inicio, end=' ')
            inicio += passo
    sleep(0.5)
    print('FIM!')
#  Programa principal:
lin()
contador(1, 10, 1)
lin()
contador(10, 0, -2)
lin()
print('Agora é a sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Final: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
lin()
