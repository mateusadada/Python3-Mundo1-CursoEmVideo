# Crie um script que leia o nome, a idade e o peso de uma pessoa e mostre na tela.

print('Bem-vindo ao programa que exibe o nome, a idade e o peso de uma pessoa!')

nome = input('Qual é o seu nome? ')
idade = input('Qual é a sua idade? ')
peso = input('Qual é o seu peso? ')

print(f'\nNome: \033[33m{nome}\033[m'
      f'\nIdade: \033[33m{idade}\033[m anos'
      f'\nPeso: \033[33m{peso}\033[m kg')
