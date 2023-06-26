# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

print('Bem vindo ao programa de cálculo de aumento de salário!')

salario = float(input('Qual é o salário do funcionário? R$ '))
novo_salario = salario * 1.15

print(f'\nUm funcionário que ganhava R$ {salario:.2f} reais, com 15% de aumento, passa a receber RS {novo_salario:.2f} reais')
