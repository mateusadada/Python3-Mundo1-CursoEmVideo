print('Bem-vindo ao programa que adiciona underline no nome!')

nome = input('Qual é o seu nome? ')

print(f'\nPrazer em te conhecer, \033[33m{nome:_<20}\033[m!')
print(f'Prazer em te conhecer, \033[33m{nome:_>20}\033[m!')
print(f'Prazer em te conhecer, \033[33m{nome:_^20}\033[m!')
