frase = 'Curso em Vídeo Python'  # Determinar objeto
### FATIAMENTO
frase[1] # O primeiro caractér não é o 1, mas o 0.
frase[0:6] == frase[:6]  # Se omitir o valor, então ele vai considerar o primeiro/último caracter.
frase[9:21] == frase[9:]  ### NOTA: A ÚLTIMA POSIÇÃO DO FATIAMENTO (nesse caso, 21) NÃO É CONTADA!
frase[:6:2] == frase[0:6:2]  # O terceiro número refere-se a quantas casas vão ser puladas.
frase[::3]

### ANÁLISE
len(frase)  # Tamanho do objeto.
frase.count('o')  # Contar quantos 'o' existem no objeto frase.
frase.count('o', 0, 13)  # Contar quantos 'o' existem no objeto frase, entre as posições 0 e 13.
                         ### NOTA: A POSIÇÃO 13 (ÚLTIMA DO FATIAMENTO) NÃO É CONTADA!
frase.find('deo')  # Indica aonde começa o trecho 'deo'.
frase.find('w')  # Caso não exista, ele retorna -1.
var = 'Curso' in frase  # Operador booleano

### TRANSFORMAÇÃO
frase.replace('Python', 'Android')  # Procurar por 'Python' e substituir por 'Android'
frase.upper()  # Transforma tudo em maiúsculo
frase.lower()  # Transforma tudo em minúsculo
frase.capitalize()  # Transforma tudo em minúsculo e transforma a primeira letra em maiúscula.
frase.title()  # Transforma tudo em minúsculo, e transforma a primeira letra de cada palavra em maiúscula.
frase.strip()  # Remove espaços sobrando antes e depois da string.
               # VARIAÇÕES:
               frase.rstrip()  # Tira só os espaços da direita
               frase.lstrip()  # Tira só os espaços da esquerda

### DIVISÃO (FORMA UMA LISTA)
frase.split()  # Divide a frase em pedaços (por padrão, nos espaços). frase.split('e') separa na letra 'e'.

### JUNÇÃO (JUNTA UMA LISTA EM UM STRING)
'-'.join(frase) # Após um split, junta tudo com um '-' (pode mudar para outras coisas).

### PRINT
print("""
Oi
Pessoal
""")  # Três aspas printa exatamente da forma escrita.

### CONCATENAR FUNÇÕES
print(frase.upper().count("O"))  # Pode simplesmente colocar uma função depois da outra com o ".".
