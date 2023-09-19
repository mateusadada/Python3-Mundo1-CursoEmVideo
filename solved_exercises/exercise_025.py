# Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

print('Bem-vindo ao programa que verifica se tem "SILVA" no nome de uma pessoa!')

nome = str(input('Nome completo: ')).strip()

print(f'\nTem SILVA no nome? \033[33m{"SILVA" in nome.upper()}\033[m')
