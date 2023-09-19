# Leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

print('Bem-vindo ao programa que exibe várias informações a partir de algo digitado!')

dado = input('Digite algo: ')

print(f'\nO tipo primitivo desse valor é \033[33m{type(dado)}\033[m')
print(f'Só tem espaços? \033[33m{dado.isspace()}\033[m')
print(f'É um número? \033[33m{dado.isnumeric()}\033[m')
print(f'É alfabético? \033[33m{dado.isalpha()}\033[m')
print(f'É alfanumérico? \033[33m{dado.isalnum()}\033[m')
print(f'Está em maiúsculas? \033[33m{dado.isupper()}\033[m')
print(f'Está em minúsculas? \033[33m{dado.islower()}\033[m')
print(f'Está capitalizada? \033[33m{dado.istitle()}\033[m')
