# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

dinheiro = float(input('Quanto dinheiro você tem na carteira? R$ '))

dolares = dinheiro / 5.30
euro = dinheiro / 5.74
iene = dinheiro / 24.67

print(f'\nCom R$ {dinheiro:.2f} reais você pode comprar:'
      f'\nUS$ {dolares:.2f} dólares'
      f'\nEUR {euro:.2f} euros'
      f'\nJPY {iene:.2f} ienes')
