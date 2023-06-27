# Crie um programa que leia o nome completo de uma pessoa e mostre:
# – O nome com todas as letras maiúsculas e minúsculas.
# – Quantas letras no total (sem considerar espaços).
# – Quantas letras tem o primeiro nome.

print('Bem vindo ao programa que faz várias análises a partir de um nome!')

nome = input('Nome completo: ')

primeiro_nome = nome.split()

print(f'\nLetras maiúsculas: {nome.upper()}'
      f'\nMinúsculas: {nome.lower()}'
      f'\nTotal de letras (sem espaços): {len(nome.replace(" ", ""))}'
      f'\nLetras no primeiro nome: {len(primeiro_nome[0])}')
