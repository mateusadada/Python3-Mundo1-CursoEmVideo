print('Bem-vindo ao programa que faz uma saudação ao nome!')

nome = str(input('Qual é o seu nome? ')).strip()

if nome == 'Mateus':
    print('\n\033[33mQue nome lindo você tem!\033[m')
else:
    print('\n\033[33mSeu nome é tão normal!\033[m')

print(f'Bom dia, \033[33m{nome}\033[m!')
