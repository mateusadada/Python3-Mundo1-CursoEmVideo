# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

print('Bem vindo ao programa de cálculo que exibe o dobro, o triplo e a raiz quadrada de um número!')

numero = int(input('Digite um número: '))

print(f'\nDobro: {numero * 2}')
print(f'Triplo: {numero * 3}')
print(f'Raiz quadrada: {numero ** (1/2):.2f}')
