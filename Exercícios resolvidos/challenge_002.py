# Crie um script que leia o dia, o mês e o ano de nascimento de uma pessoa e mostre uma mensagem com a data formada.

print('Bem vindo ao programa que exibe o dia, o mês e o ano de nascimento de uma pessoa!')

dia = input('Qual o dia do seu nascimento? ')
mes = input('Qual o mês? ')
ano = input('Qual o ano? ')

print(f'Você nasceu no dia \033[33m{dia}\033[m de \033[33m{mes}\033[m de \033[33m{ano}\033[m, correto?')
