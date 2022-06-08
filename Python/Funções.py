# define-se uma função assim:
def lin():
    print('-' * 30)


def mensagem(msg):
    lin()
    print(msg)
    lin()


def contador(*num):  # cria uma tupla chamada num com todos argumentos que forem passados na função.
    tam = len(num)
    print(tam)


def soma(*num):  # o asterisco marca um desenpacotamento (isto é, o que eu fizer com num não vai afetar o objeto que
    total = sum(num)     # passou como argumento lá no programa principal.
    print(total)


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1
    print(lst)


# Devemos colocar duas linhas entre as definições e o programa principal:
mensagem('Parabéns!')
contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)
soma(2, 1, 7)
soma(8, 0)
soma(4, 4, 7, 6, 2)
valores = [2, 1, 7, 8, 0, 4, 4, 7, 6, 2]
dobra(valores)
print(valores)  # Qualquer coisa que eu fizer com valores, vai afetar o objeto original (isso não é desenpacotamento).

###  Interactive help
# Digitando:
help()
#  A gente abre a seção de ajuda.
#  Para sair digitar:
quit
#  Outra forma é obtendo o .doc da função:
print(input.__doc__)  # docstring
help(input)
#  Docstrings: explica funcionalidades de uma função.
#  Para criar uma docstring inserir aspas duplas três vezes logo abaixo da linha def:


def contador(i, f, p):
    """
    Conta de i (início) até f (final) de p em p (passo).
    Ex.: contador(0,10,2)
         > 0, 2, 4, 6, 8, 10
    Quando o passo está ausente, a função considera passo igual a 1.
    :param i: O início da contagem.
    :param f: O fim da contagem.
    :param p: O passo a ser dado na contagem.
    :return: Uma lista com os valores solicitados.
    """
    resultado = list()
    c = i
    while c <= f:
        resultado.append(c)
        c += p
    return resultado


c = contador(0, 10, 2)
print(c)
print(type(c))
help(contador)

### Escopos:
# É possível, como no R, usar a mesma denominação para variáveis no escopo global e no escopo local da função.
# Se quiser, da pra pedir pra função usar a mesma variável do escopo global.
# Aí o objeto no escopo global recebe o mesmo valor de dentro da função.
def teste(b):
    global a
    a = 8
    b += 5
    print(f'a = {a}')
    print(f'b = {b}')


a = 4
teste(a)

### Return:
# 
