# Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem, cobrando R$ 0,50
# por km para viagens de até 200 km e R$ 0,45 parta viagens mais longas.

print('Bem-vindo ao programa de cálculo de passagem!')

distancia = int(input('Informe a distância (km): '))

if distancia <= 200:
    print(f'\nPassagem (R$ 0,50 por km): R$ \033[33m{distancia * 0.5:.2f}\033[m reais')
else:
    print(f'\nPassagem (R$ 0,45 por km): R$ \033[33m{distancia * 0.45:.2f}\033[m reais')
