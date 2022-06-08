# tratamento de erros e exceções pode ser feito por um try:
try:
    a = int(input('Digite o numerador: '))
    b = int(input('Digite o denominador: '))
    r = a/b
except (ValueError, TypeError):  # tipo de erro, erro de digitação
    print('Tivemos um problema com os tipos de dados que você digitou.')
except ZeroDivisionError:  # erro de divisão por zero
    print('Não é possível dividir um número por zero.')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados.')
else:  # o que deve acontecer caso o try funcione.
    print(f'O resultado é {r}.')
finally:  # vai acontecer de qualquer jeito.
    print('Até a próxima!')
