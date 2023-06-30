# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

print('Bem-vindo ao programa que exibe na tela os dígitos separados de um número!')

# primeiro print
numero = str(input('Digite um número (0 a 9999): '))
# segundo print
numero_convertido = int(numero)

print(f'\n1º dígito: \033[33m{numero[0:1]}\033[m'
      f'\n2º dígito: \033[33m{numero[1:2]}\033[m'
      f'\n3º dígito: \033[33m{numero[2:3]}\033[m'
      f'\n4º dígito: \033[33m{numero[3:4]}\033[m')

print(f'\nUnidade: \033[33m{numero_convertido % 10}\033[m'
      f'\nDezena: \033[33m{(numero_convertido // 10) % 10}\033[m'
      f'\nCentena: \033[33m{(numero_convertido // 100) % 10}\033[m'
      f'\nMilhar: \033[33m{(numero_convertido // 1000) % 10}\033[m')
