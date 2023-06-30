# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar
# descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu
# ou perdeu.

from random import randint

print('Bem-vindo ao programa de adivinhação de número!')

numero_sorteado = randint(1, 5)

while True:
    numero_escolhido = int(input('Digite um número entre 0 e 5: '))

    if numero_escolhido < 0 or numero_escolhido > 5:
        print('\033[33mNúmero inválido! Tente novamente\n\033[m')
    else:
        break

if numero_escolhido == numero_sorteado:
    print('\n\033[32mParabéns, você acertou!\033[m')
else:
    print('\n\033[31mInfelizmente, não foi dessa vez :(\033[m'
          f'\n\033[31mO número sorteado foi {numero_sorteado}\033[m')
