# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele
# lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
# import random

from random import choice

print('Bem-vindo ao programa de sorteio de nome para apagar o quadro!')

nome_1 = input('*** Informe os nomes ***'
               '\n1º aluno: ')
nome_2 = input('2º aluno: ')
nome_3 = input('3º aluno: ')
nome_4 = input('4º aluno: ')

sorteado = choice([nome_1, nome_2, nome_3, nome_4])

print(f'\nO aluno escolhido foi \033[33m{sorteado}\033[m')
