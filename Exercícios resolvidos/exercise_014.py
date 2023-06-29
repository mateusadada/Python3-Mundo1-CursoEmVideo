# Escreva um programa que converta uma temperatura digitado em graus Celsius e converta para graus Fahrenheit.

print('Bem vindo ao programa de conversão de celsius em fahrenheit!')

graus_celsius = float(input('Informe a temperatura em ºC: '))
graus_fahrenheit = 1.8 * graus_celsius + 32

print(f'\nA temperatura de \033[33m{graus_celsius}\033[mºC corresponde a \033[33m{graus_fahrenheit:.1f}\033[mºF!')
