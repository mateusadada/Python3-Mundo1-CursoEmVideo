# Leia um valor em metros e o exiba convertido em centímetros e milímetros.

print('Bem-vindo ao programa de conversão de centímetros e milímetros!')

valor = float(input('Digite um valor (metros): '))
centimetro = valor * 100
milimetro = valor * 1000

print(f'\nConversão \033[33m{centimetro:.2f}\033[m centímetros')
print(f'Conversão \033[33m{milimetro:.2f}\033[m milímetros')
