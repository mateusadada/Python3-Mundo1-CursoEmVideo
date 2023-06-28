# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome
# separadamente.

print('Bem vindo ao programa que exibe o primeiro e o último nome separadamente!')

nome = str(input('Nome completo: ')).strip()
nome_convertido = nome.split()

print(f'\nPrimeiro nome: {nome_convertido[0]}'
      f'\nÚltimo nome: {nome_convertido[len(nome_convertido) - 1]}')
