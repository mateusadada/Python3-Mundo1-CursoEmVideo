# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input('Qual é o preço do produto? R$ '))

preco_com_desconto = preco * 0.95

print(f'\nO produto que custava R$ {preco:.2f}, na promoção com desconto de 5% vai custar R$ {preco_com_desconto:.2f}')
