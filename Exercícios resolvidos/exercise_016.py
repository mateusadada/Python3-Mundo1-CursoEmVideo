# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.
# Ex: Digite um número: 6.127
# O número 6.127 tem a parte inteira 6.

print('Bem vindo ao programa que exibe a parte inteira de um número fracionado!')

numero = float(input('Digite um valor: '))

print(f'\nO número \033[33m{numero}\033[m tem a parte inteira \033[33m{int(numero)}\033[m')
