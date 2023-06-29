# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários
# superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

print('Bem vindo ao programa de cálculo de aumento de salário!')

salario = float(input('Informe o salário: R$ '))

if salario > 1250:
    print(f'\nAumento de 10%!'
          f'\nNovo salário: R$ {salario * 1.1:.2f} reais')
else:
    print(f'\nAumento de 15%!'
          f'\nNovo salário: R$ {salario * 1.15:.2f} reais')
