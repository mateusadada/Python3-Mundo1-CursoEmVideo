# Faça um programa que leia uma frase pelo teclado e mostre:
# - Quantas vezes aparece a letra “A”;
# - A posição que ela aparece a primeira vez;
# - A posição que ela aparece a última vez.

print('Bem vindo ao programa que exibe várias informações a partir de uma frase!')

frase = str(input('Digite uma frase: ')).strip()

print(f'\nQuantas vezes aparece a letra "a/A": {frase.lower().count("a")}'
      f'\nA posição que aparece por primeiro: {frase.lower().find("a") + 1}'
      f'\nA posição que aparece por último: {frase.lower().rfind("a") + 1}')
