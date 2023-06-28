# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

print('Bem vindo ao programa de cálculo de ano bissexto!')

ano = int(input('Digite um ano: '))

if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0:
            print(f'\nO ano {ano} é bissexto!')
        else:
            print(f'\nO ano {ano} é NÃO bissexto!')
    else:
        print(f'\nO ano {ano} é bissexto!')
else:
    print(f'\nO ano {ano} é NÃO bissexto!')
