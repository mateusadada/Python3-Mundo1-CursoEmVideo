# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
# Usar Python Packages

from math import radians, sin, cos, tan

print('Bem vindo ao programa de cálculo de seno, cosseno e tangente!')

angulo_graus = float(input('Digite um ângulo: '))

angulo_radiano = radians(angulo_graus)

print(f'\nO ângulo de \033[33m{angulo_graus}\033[m° tem as seguintes características:'
      f'\n- Seno: \033[33m{sin(angulo_radiano):.2f}\033[m'
      f'\n- Cosseno: \033[33m{cos(angulo_radiano):.2f}\033[m'
      f'\n- Tangente: \033[33m{tan(angulo_radiano):.2f}\033[m')
