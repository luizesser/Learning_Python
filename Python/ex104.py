def leiaint():
    while True:
        t = input('Digite um número: ')
        if t.isnumeric():
            print(f'Você digitou o número {t}.')
            return int(t)
        else:
            print("ERRO! Digite um número inteiro.")


leiaint()
