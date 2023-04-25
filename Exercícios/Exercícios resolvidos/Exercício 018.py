# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
# Usar Python Packages

from math import radians, sin, cos, tan

print('Bem vindo! Este programa mostra o valor do seno, cosseno e tangente de qualquer ângulo.')

angulo_graus = float(input('Digite um ângulo: '))

angulo_radiano = radians(angulo_graus)

print(f'\nO ângulo de {angulo_graus}° tem as seguintes características:'
      f'\n- Seno: {sin(angulo_radiano):.2f}'
      f'\n- Cosseno: {cos(angulo_radiano):.2f}'
      f'\n- Tangente: {tan(angulo_radiano):.2f}')
