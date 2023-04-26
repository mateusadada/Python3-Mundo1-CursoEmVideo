import random

print('Bem vindo ao programa que sorteia um número entre 1 e 100 e entre 0 e 1!')

numero = random.randint(1, 100)
numero2 = random.random()

print(f'Entre 1 e 100: {numero}'
      f'\nEntre 0 e 1: {numero2}')
