# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

print('Bem-vindo ao programa de cálculo da média de duas notas!')

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2)/2

print(f'\nA média entre \033[33m{nota1}\033[m e \033[33m{nota2}\033[m é igual a \033[33m{media:.2f}\033[m')
