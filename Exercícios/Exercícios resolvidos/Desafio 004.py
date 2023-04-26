# Leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele

print('Bem vindo ao programa que exibe várias informações a partir de algo digitado!')

resposta = input('Digite qualquer coisa: ')

print(f'\nQual o tipo primitido? {type(resposta)}')
print(f'É um número? {resposta.isnumeric()}')
print(f'É alfanúmerico? {resposta.isalnum()}')
print(f'Está tudo em maiúsculo? {resposta.isupper()}')
print(f'Tem espaço? {resposta.isspace()}')
print(f'Contém apenas letras? {resposta.isalpha()}')
print(f'Tem decimal? {resposta.isdecimal()}')
