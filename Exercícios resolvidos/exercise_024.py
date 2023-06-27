# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome “Santo”.

print('Bem vindo ao programa que verifica se o nome de uma cidade começa com "Santo"!')

cidade = str(input('Digite o nome de uma cidade: ')).strip()

print(f'\nO nome começa com "Santo"? {(cidade[0:5]).upper() == "SANTO"}')
