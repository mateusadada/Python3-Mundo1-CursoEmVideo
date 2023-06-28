print('Bem vindo ao programa que faz uma saudação ao nome!')

nome = str(input('Qual é o seu nome? ')).strip()

if nome == 'Mateus':
    print('\nQue nome lindo você tem!')
else:
    print('\nSeu nome é tão normal!')

print(f'Bom dia, {nome}!')
