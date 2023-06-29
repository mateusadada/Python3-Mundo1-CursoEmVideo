# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.

print('Bem vindo ao programa que exibe o sucessor e o antecessor de um número!')

numero = int(input('Digite um número: '))

print(f'\nSucessor: \033[33m{numero + 1}\033[m')
print(f'Antecessor: \033[33m{numero - 1}\033[m')
