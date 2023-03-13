# Leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco_atual = float(input('Digite o preço de um produto: R$ '))
preco_novo = preco_atual * 0.95

print(f'\nPreço com 5% de desconto: R$ {preco_novo:.2f} reais')
