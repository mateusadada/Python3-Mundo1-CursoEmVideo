# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias
# pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

print('Bem vindo ao programa de cálculo de carro alugado!')

KM = int(input('Quantos KM rodados? '))
dias = int(input('Quantos dias alugados? '))
valor = dias * 60 + KM * 0.15

print(f'\nO total a pagar é de R$ \033[33m{valor:.2f}\033[m reais')
