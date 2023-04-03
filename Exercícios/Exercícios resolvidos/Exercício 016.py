# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.
# Ex: Digite um número: 6.127
# O número 6.127 tem a parte inteira 6.

import math

numero = float(input('Digite um valor: '))

print(f'\nO número {numero} tem a parte inteira {math.floor(numero)}')
