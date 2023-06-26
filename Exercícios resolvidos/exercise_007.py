# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

print('Bem vindo ao programa de cálculo da média de duas notas!')

nota1 = float(input('Primeira nota do aluno: '))
nota2 = float(input('Segunda nota do aluno: '))
media = (nota1 + nota2)/2

print(f'\nA média entre {nota1:.1f} e {nota2:.1f} é igual a {media:.1f}')
