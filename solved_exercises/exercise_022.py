# Crie um programa que leia o nome completo de uma pessoa e mostre:
# – O nome com todas as letras maiúsculas e minúsculas.
# – Quantas letras no total (sem considerar espaços).
# – Quantas letras tem o primeiro nome.

print('Bem-vindo ao programa que faz várias análises a partir de um nome!')

nome = str(input('Nome completo: ')).strip()

primeiro_nome = nome.split()

print(f'\nLetras maiúsculas: \033[33m{nome.upper()}\033[m'
      f'\nMinúsculas: \033[33m{nome.lower()}\033[m'
      f'\nTotal de letras (sem espaços): \033[33m{len(nome.replace(" ", ""))}\033[m'
      f'\nLetras no primeiro nome: \033[33m{len(primeiro_nome[0])}\033[m')
