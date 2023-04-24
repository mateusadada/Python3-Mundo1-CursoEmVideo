# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
# Calcule e mostre o comprimento da hipotenusa.
# H² = CA² + CO²
# Usar Python Packages

from math import hypot

print('Bem vindo! Este programa calcula a hipotenusa de um triângulo retângulo.')

cateto_oposto = float(input('Comprimento do cateto oposto: '))
cateto_adjacente = float(input('Comprimento do cateto adjacente: '))

hipotenusa = hypot(cateto_oposto, cateto_adjacente)

print(f'\nA hipotenusa mede {hipotenusa:.2f}')
