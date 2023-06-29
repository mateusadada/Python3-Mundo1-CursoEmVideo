print('Bem vindo ao programa que verifica se um texto possui apenas espaço!')

numero1 = input('Digite algo: ')

print(f'\nTem apenas espaço? \033[33m{numero1.isspace()}\033[m')
