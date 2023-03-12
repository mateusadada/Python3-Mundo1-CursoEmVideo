# Leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. 1 US$ = R$ 3.27

dinheiro = float(input('Quanto dinheiro você tem? R$ '))
dolares = dinheiro / 3.27

print(f'\nCom R$ {dinheiro:.2f} reais você pode comprar US$ {dolares:.2f} dólares')
