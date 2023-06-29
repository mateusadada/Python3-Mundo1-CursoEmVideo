# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

print('Bem vindo ao programa de cálculo que exibe o dobro, o triplo e a raiz quadrada de um número!')

numero = int(input('Digite um número: '))

print(f'\nDobro: \033[33m{numero * 2}\033[m')
print(f'Triplo: \033[33m{numero * 3}\033[m')
print(f'Raiz quadrada: \033[33m{numero ** (1/2):.2f}\033[m')
