# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

print('Bem vindo ao programa de cálculo do maior e menor número!')

numero = []

for i in list(range(3)):
    numero.append(int(input(f'{i + 1}º número: ')))

maior = numero[0]
menor = numero[0]

for i in list(range(1, 3)):
    if numero[i] > maior:
        maior = numero[i]

    if numero[i] < menor:
        menor = numero[i]

print(f'\nMaior: \033[33m{maior}\033[m'
      f'\nMenor: \033[33m{menor}\033[m')
