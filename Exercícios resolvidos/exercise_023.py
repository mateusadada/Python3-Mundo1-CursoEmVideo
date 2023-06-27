# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

print('Bem vindo ao programa que exibe na tela os dígitos separados de um número!')

# primeiro print
numero = str(input('Digite um número (0 a 9999): '))
# segundo print
numero_convertido = int(numero)

print(f'\n1º dígito: {numero[0:1]}'
      f'\n2º dígito: {numero[1:2]}'
      f'\n3º dígito: {numero[2:3]}'
      f'\n4º dígito: {numero[3:4]}')

print(f'\nUnidade: {numero_convertido % 10}'
      f'\nDezena: {(numero_convertido // 10) % 10}'
      f'\nCentena: {(numero_convertido // 100) % 10}'
      f'\nMilhar: {(numero_convertido // 1000) % 10}')
