# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

print('Bem-vindo ao programa de cálculo da média de duas notas!')

nota1 = float(input('Primeira nota do aluno: '))
nota2 = float(input('Segunda nota do aluno: '))
media = (nota1 + nota2)/2

print(f'\nA média entre \033[33m{nota1:.1f}\033[m e \033[33m{nota2:.1f}\033[m é igual a \033[33m{media:.1f}\033[m')
