# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

print('Bem-vindo ao programa de cálculo de par ou ímpar!')

numero = int(input('Digite um número inteiro: '))

if numero % 2 == 0:
    print(f'\nO número \033[33m{numero}\033[m é PAR')
else:
    print(f'\nO número \033[33m{numero}\033[m é ÍMPAR')
