# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que
# ele foi multado. A multa vai custar R$7,00 por cada km acima do limite.

print('Bem vindo ao programa de multas!')

velocidade = int(input('Digite a velocidade (km/h): '))

if velocidade > 80:
    print(f'\nMultado por ter excedido {velocidade - 80} km/h'
          f'\nValor a pagar: R$ {(velocidade - 80) * 7:.2f} reais')
else:
    print('\nVelocidade dentro do permitido. Liberado!')
