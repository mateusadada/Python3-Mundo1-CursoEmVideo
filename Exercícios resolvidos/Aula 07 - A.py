print('Bem vindo ao programa que adiciona underline no nome!')

nome = input('Qual é o seu nome? ')

print(f'\nPrazer em te conhecer, {nome:_<20}!')
print(f'Prazer em te conhecer, {nome:_>20}!')
print(f'Prazer em te conhecer, {nome:_^20}!')
