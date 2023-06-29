# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários
# superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

print('Bem vindo ao programa de cálculo de aumento de salário!')

salario = float(input('Informe o salário: R$ '))

if salario > 1250:
    print(f'\nAumento de \033[33m10%!\033[m'
          f'\nNovo salário: R$ \033[33m{salario * 1.1:.2f}\033[m reais')
else:
    print(f'\nAumento de \033[33m15%!\033[m'
          f'\nNovo salário: R$ \033[33m{salario * 1.15:.2f}\033[m reais')
