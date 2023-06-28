# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$ 0,50
# por km para viagens de até 200 km e R$ 0,45 parta viagens mais longas.

print('Bem vindo ao programa de cálculo de passagem!')

distancia = int(input('Informe a distância (km): '))

if distancia <= 200:
    print(f'\nPassagem (R$ 0,50 por km): R$ {distancia * 0.5:.2f} reais')
else:
    print(f'\nPassagem (R$ 0,45 por km): R$ {distancia * 0.45:.2f} reais')
