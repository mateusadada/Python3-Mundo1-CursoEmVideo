# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que
# ele foi multado. A multa vai custar R$7,00 por cada km acima do limite.

print('Bem vindo ao programa de multas!')

velocidade = int(input('Digite a velocidade (km/h): '))

if velocidade > 80:
    print(f'\n\033[31mMultado\033[33m por ter excedido {velocidade - 80} km/h\033[m'
          f'\n\033[33mValor a pagar: R$ \033[31m{(velocidade - 80) * 7:.2f}\033[33m reais\033[m')
else:
    print('\n\033[33mVelocidade dentro do permitido. Liberado!\033[m')
