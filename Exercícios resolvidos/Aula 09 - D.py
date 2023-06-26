print('Bem vindo ao programa de divisão de string!\n')

frase = 'Curso em Vídeo Python'

print(frase)

# separa as palavras. Recria os índices numa nova lista. Retira os espaços
frase = frase.split()
print(frase)

# junta as palavras/listas
frase = ' '.join(frase)
print(frase)
