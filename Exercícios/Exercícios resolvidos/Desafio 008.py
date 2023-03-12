# Leia um valor em metros e o exiba convertido em centímetros e milímetros.

valor = float(input('Digite um valor (metros): '))
centimetro = valor * 100
milimetro = valor * 1000

print(f'\nConversão {centimetro:.2f} centímetros')
print(f'Conversão {milimetro:.2f} milímetros')
