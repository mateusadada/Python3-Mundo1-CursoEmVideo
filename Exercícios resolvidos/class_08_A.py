from math import sqrt, floor

print('Bem-vindo ao programa de cálculo de raiz quadrada!')

numero = int(input('Digite um número: '))
raiz_quadrada = sqrt(numero)

print(f'\nA raiz quadrada de \033[33m{numero}\033[m é \033[33m{floor(raiz_quadrada)}\033[m')
