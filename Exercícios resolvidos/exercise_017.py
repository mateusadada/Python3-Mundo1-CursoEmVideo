# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
# Calcule e mostre o comprimento da hipotenusa.
# H² = CA² + CO²
# Usar Python Packages

from math import hypot

print('Bem vindo ao programa de cálculo da hipotenusa de um triângulo retângulo!')

cateto_oposto = float(input('Comprimento do cateto oposto: '))
cateto_adjacente = float(input('Comprimento do cateto adjacente: '))

hipotenusa = hypot(cateto_oposto, cateto_adjacente)

print(f'\nA hipotenusa mede \033[33m{hipotenusa:.2f}\033[m')
