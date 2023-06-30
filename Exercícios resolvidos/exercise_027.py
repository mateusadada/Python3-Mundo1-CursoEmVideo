# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome
# separadamente.

print('Bem-vindo ao programa que exibe o primeiro e o último nome separadamente!')

nome = str(input('Nome completo: ')).strip().split()

print(f'\nPrimeiro nome: \033[33m{nome[0]}\033[m'
      f'\nÚltimo nome: \033[33m{nome[len(nome) - 1]}\033[m')
