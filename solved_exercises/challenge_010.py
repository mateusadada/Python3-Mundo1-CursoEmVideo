# Leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. 1 US$ = R$ 3.27

print('Bem-vindo ao programa de conversão de reais em dólares!')

dinheiro = float(input('Quanto dinheiro você tem? R$ '))
dolares = dinheiro / 3.27

print(f'\nCom R$ \033[33m{dinheiro:.2f}\033[m reais você pode comprar US$ \033[33m{dolares:.2f}\033[m dólares')
