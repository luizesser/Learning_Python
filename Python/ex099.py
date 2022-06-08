def linha():
    print('-'*30)


def maior(*num):
    lst = list(num)
    print(f'Você informou os valores {lst}.')
    print(f'Um total de {len(lst)} valores')
    m = 0
    for v in range(0, len(lst)):
        if v == 0:
            m = lst[v]
        else:
            if lst[v] > m:
                m = lst[v]
    print(f'O maior valor é o {m}')
    linha()


maior(1, 2, 3, 4, 5, 6, 7)
maior(0, 7, 4, 2, 6, 4, 0)
maior(-6, -908, 105, 105.7, 99)
maior()
