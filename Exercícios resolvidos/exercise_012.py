# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

print('Bem vindo ao programa de cálculo de desconto de um produto!')

preco = float(input('Qual é o preço do produto? R$ '))
preco_com_desconto = preco * 0.95

print(f'\nO produto que custava R$ \033[33m{preco:.2f}\033[m, na promoção com desconto de 5% vai custar R$ '
      f'\033[33m{preco_com_desconto:.2f}\033[m')
