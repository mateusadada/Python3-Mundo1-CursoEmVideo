print('Bem vindo ao programa de análise de string!\n')

# 20 índices e 21 caracteres
frase = 'Curso em Vídeo Python'

# quantidade de índices/tamanho
print('\033[33m', len(frase))

# quantidade de 'o'
print(frase.count('o'))

# quantidade de 'o' do índice 0 até o 12
print(frase.count('o', 0, 13))

# mostra a posição/índice que começa 'deo'
print(frase.find('deo'))

# se a string não existe = -1
print(frase.find('Android'))

# se 'Curso' tem na variável frase
print('Curso' in frase)

# não substitui direto na variável
print(frase.replace('Python', 'Android'))

# deixa tudo em maiúsculo. Colocar os () porque é método
print(frase.upper())

# deixa tudo em minúsculo
print(frase.lower())

# tudo em minúsculo, menos o índice 0
print(frase.capitalize())

# cada início de palavra fica em maiúscula
print(frase.title())
