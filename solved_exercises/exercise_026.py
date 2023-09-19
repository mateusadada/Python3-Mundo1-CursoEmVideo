# Faça um programa que leia uma frase pelo teclado e mostre:
# - Quantas vezes aparece a letra “A”;
# - A posição que ela aparece a primeira vez;
# - A posição que ela aparece a última vez.

print('Bem-vindo ao programa que exibe várias informações a partir de uma frase!')

frase = str(input('Digite uma frase: ')).lower().strip()

print(f'\nQuantas vezes aparece a letra "a/A": \033[33m{frase.count("a")}\033[m'
      f'\nA posição que aparece por primeiro: \033[33m{frase.find("a") + 1}\033[m'
      f'\nA posição que aparece por último: \033[33m{frase.rfind("a") + 1}\033[m')
