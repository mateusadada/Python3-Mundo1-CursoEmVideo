# Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.

print('Bem-vindo ao programa que exibe a tabuada de um número!')

numero = int(input('Digite um número para ver sua tabuada: '))

print(f'\n------------' 
      f'\n{numero} x {1:2} = \033[33m{numero * 1}\033[m'
      f'\n{numero} x {2:2} = \033[33m{numero * 2}\033[m'
      f'\n{numero} x {3:2} = \033[33m{numero * 3}\033[m'
      f'\n{numero} x {4:2} = \033[33m{numero * 4}\033[m'
      f'\n{numero} x {5:2} = \033[33m{numero * 5}\033[m'
      f'\n{numero} x {6:2} = \033[33m{numero * 6}\033[m'
      f'\n{numero} x {7:2} = \033[33m{numero * 7}\033[m'
      f'\n{numero} x {8:2} = \033[33m{numero * 8}\033[m'
      f'\n{numero} x {9:2} = \033[33m{numero * 9}\033[m'
      f'\n{numero} x {10:2} = \033[33m{numero * 10}\033[m'
      f'\n------------')
