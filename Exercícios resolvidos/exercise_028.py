# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar
# descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu
# ou perdeu.

from random import randint

print('Bem vindo ao programa de adivinhação de número!')

numero_sorteado = randint(1, 5)

while True:
    numero_escolhido = int(input('Digite um número entre 0 e 5: '))

    if numero_escolhido < 0 or numero_escolhido > 5:
        print('Número inválido! Tente novamente\n')
    else:
        break

if numero_escolhido == numero_sorteado:
    print('\nParabéns, você acertou!')
else:
    print('\nInfelizmente, não foi dessa vez :('
          f'\nO número sorteado foi {numero_sorteado}')
