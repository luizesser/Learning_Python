exp = list(input('Digite a expressão: '))
count = 0
for i in exp:
    if i == '(':
        count += 1
    if i == ')':
        count -= 1
    if count < 0:
        break
if count != 0:
    print('Sua expressão é inválida!')
else:
    print('Sua expressão é válida!')
