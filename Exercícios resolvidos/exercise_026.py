# Faça um programa que leia uma frase pelo teclado e mostre:
# - Quantas vezes aparece a letra “A”;
# - A posição que ela aparece a primeira vez;
# - A posição que ela aparece a última vez.

print('Bem vindo ao programa que exibe várias informações a partir de uma frase!')

frase = str(input('Digite uma frase: ')).lower().strip()

print(f'\nQuantas vezes aparece a letra "a/A": {frase.count("a")}'
      f'\nA posição que aparece por primeiro: {frase.find("a") + 1}'
      f'\nA posição que aparece por último: {frase.rfind("a") + 1}')
