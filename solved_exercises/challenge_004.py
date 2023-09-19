# Leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

print('Bem-vindo ao programa que exibe várias informações a partir de algo digitado!')

resposta = input('Digite qualquer coisa: ')

print(f'\nQual o tipo primitivo? \033[33m{type(resposta)}\033[m')
print(f'É um número? \033[33m{resposta.isnumeric()}\033[m')
print(f'É alfanúmerico? \033[33m{resposta.isalnum()}\033[m')
print(f'Está tudo em maiúsculo? \033[33m{resposta.isupper()}\033[m')
print(f'Tem espaço? \033[33m{resposta.isspace()}\033[m')
print(f'Contém apenas letras? \033[33m{resposta.isalpha()}\033[m')
print(f'Tem decimal? \033[33m{resposta.isdecimal()}\033[m')
