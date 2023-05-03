# O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import sample

print('Bem vindo ao programa que sorteia a ordem de apresentação de trabalhos!')

alunos = []

for e in range(0, 4):
    alunos.append(input(f'Nome do {e + 1}º aluno: '))

print('\nA ordem de apresentação será:'
      f'\n{sample(alunos, k=4)}')
