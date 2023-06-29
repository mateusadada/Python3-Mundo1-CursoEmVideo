# Leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

print('Bem vindo ao programa de cálculo de desconto de um produto!')

preco_atual = float(input('Digite o preço: R$ '))
preco_novo = preco_atual * 0.95

print(f'\nPreço com 5% de desconto: R$ \033[33m{preco_novo:.2f}\033[m reais')
