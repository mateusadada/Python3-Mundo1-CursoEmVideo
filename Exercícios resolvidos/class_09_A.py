print('Bem-vindo ao programa de fatiamento de string!\n')

# 20 índices e 21 caracteres
frase = 'Curso em Vídeo Python'

# do 9 até o 12
# o último valor não entra na contagem (13 - 1 = 12)
print('\033[33m', frase[9:13])

# do 9 até o 20
print(frase[9:21])

# pulando a cada dois
print(frase[9:21:2])

# do 0 até o 4 (não sei aonde começa)
print(frase[:5])

# do 15 até o final (não sei o limite)
print(frase[15:])

# do 9 até o final (não sei qual) pulando 3
print(frase[9::3])
