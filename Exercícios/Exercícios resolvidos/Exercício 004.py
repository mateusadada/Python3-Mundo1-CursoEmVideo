# Leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

print('Bem vindo ao programa que exibe várias informações a partir de algo digitado!')

dado = input('Digite algo: ')

print(f'\nO tipo primitivo desse valor é {type(dado)}')
print(f'Só tem espaços? {dado.isspace()}')
print(f'É um número? {dado.isnumeric()}')
print(f'É alfabético? {dado.isalpha()}')
print(f'É alfanumérico? {dado.isalnum()}')
print(f'Está em maiúsculas? {dado.isupper()}')
print(f'Está em minúsculas? {dado.islower()}')
print(f'Está capitalizada? {dado.istitle()}')
