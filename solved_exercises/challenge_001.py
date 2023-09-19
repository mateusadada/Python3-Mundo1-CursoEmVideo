# Crie um script que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas conforme o valor digitado.

print('Bem-vindo ao programa que faz uma saudação com o nome da pessoa!')

nome = input('Qual é o seu nome? ')

print(f'Olá, \033[33m{nome}\033[m! Seja bem-vindo!')
