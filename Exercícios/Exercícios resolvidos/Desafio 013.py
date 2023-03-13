# Leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario_antigo = float(input('Digite o salário do funcionário: R$ '))
salario_novo = salario_antigo * 1.15

print(f'\nNovo salário com aumento de 15%: R$ {salario_novo:.2f} reais')
