# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

print('Bem vindo ao programa de conversão de reais em dólares!')

dinheiro = float(input('Quanto dinheiro você tem na carteira? R$ '))
dolares = dinheiro / 5.30
euro = dinheiro / 5.74
iene = dinheiro / 24.67

print(f'\nCom R$ \033[33m{dinheiro:.2f}\033[m reais você pode comprar:'
      f'\nUS$ \033[33m{dolares:.2f}\033[m dólares'
      f'\nEUR \033[33m{euro:.2f}\033[m euros'
      f'\nJPY \033[33m{iene:.2f}\033[m ienes')
