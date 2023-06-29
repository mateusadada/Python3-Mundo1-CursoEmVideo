# Leia a largura e a altura de uma parede em metros, calcule a área e a quantidade de tinta necessária para pintá-la.
# Sabendo que cada litro de tinta pinta uma área de 2 m².

print('Bem vindo ao programa de cálculo de tinta para pintar uma parede!')

largura = float(input('Digite a largura: '))
altura = float(input('Digite a altura: '))
area = largura * altura
tinta_necessaria = area / 2

print(f'\nÁrea: \033[33m{area:.2f}\033[m m²')
print(f'Tinta necessária: \033[33m{tinta_necessaria:.2f}\033[m')
