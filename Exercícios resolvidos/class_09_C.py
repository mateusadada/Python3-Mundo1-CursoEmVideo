print('Bem vindo ao programa de transformação de string!\n')

frase = '   Aprenda Python  '

print('\033[33m', frase)

# remove os espaços excedentes
print(frase.strip())

# remove os espaços da direita
print(frase.rstrip())

# remove os espaços da esquerda
print(frase.lstrip())
