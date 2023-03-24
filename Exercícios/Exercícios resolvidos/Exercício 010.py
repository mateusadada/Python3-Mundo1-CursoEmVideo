# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

dinheiro = float(input('Quanto dinheiro você tem na carteira? R$ '))

dolares = (dinheiro / 3.27)

print(f'\nCom R$ {dinheiro:.2f} reais você pode comprar US$ {dolares:.2f} dólares')
