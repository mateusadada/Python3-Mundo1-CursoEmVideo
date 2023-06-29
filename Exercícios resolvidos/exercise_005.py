# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.

print('Bem vindo ao programa que exibe o sucessor e o antecessor de um número!')

numero = int(input('Digite um número: '))
antecessor = numero - 1
sucessor = numero + 1

print(f'\nAnalisando o valor \033[33m{numero}\033[m, seu antecessor é \033[33m{antecessor}\033[m e o sucessor é '
      f'\033[33m{sucessor}\033[m')
