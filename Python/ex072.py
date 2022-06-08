n2 = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
      'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
      'doze', 'treze', 'quatorze', 'quinze', 'dezeseis',
      'dezesete', 'dezoito', 'dezenove', 'vinte')
cont = 'S'
print('=' * 30)
while cont == 'S':
      n = int(input('Digite um número entre 0 e 20:'))
      if n >= 0 and n <= 20:
            print(f'Você digitou o número {n2[n]}.')
            cont = str(input('Deseja digitar mais um número [S/N]? ')).upper().strip()[0]
            print('=' * 30)
      else:
            print('Tente novamente. ', end='')
print('PROOGRAMA ENCERRADO')
