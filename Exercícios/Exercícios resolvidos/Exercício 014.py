# Escreva um programa que converta uma temperatura digitado em graus Celsius e converta para graus Fahrenheit.

graus_celsius = float(input('Informe a temperatura em ºC: '))

graus_fahrenheit = 1.8 * graus_celsius + 32

print(f'\nA temperatura de {graus_celsius}ºC corresponde a {graus_fahrenheit:.1f}ºF!')
