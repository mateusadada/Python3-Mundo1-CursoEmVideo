# Leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele

resposta = input('Digite qualquer coisa: ')

print(f'\nQual o tipo primitido? {type(resposta)}')
print(f'É um número? {resposta.isnumeric()}')
