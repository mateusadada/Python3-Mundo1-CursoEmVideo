# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

print('Bem vindo ao programa de cálculo que exibe o dobro, o triplo e a raiz quadrada de um número!')

numero = int(input('Digite um número: '))
dobro = numero * 2
triplo = numero * 3
raiz_quadrada = numero ** (1/2)

print(f'\nO dobro de \033[33m{numero}\033[m vale \033[33m{dobro}\033[m'
      f'\nO triplo de \033[33m{numero}\033[m vale \033[33m{triplo}\033[m'
      f'\nA raiz quadrada de \033[33m{numero}\033[m é igual a \033[33m{raiz_quadrada:.2f}\033[m')
