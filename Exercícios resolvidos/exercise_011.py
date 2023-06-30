# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a
# quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

print('Bem-vindo ao programa de cálculo de tinta para pintar uma parede!')

largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
area = largura * altura
tinta_necessaria = area / 2

print(f'\nSua parede tem a dimensão de \033[33m{largura}\033[m x \033[33m{altura}\033[m e sua área é de '
      f'\033[33m{area}\033[m m².'
      f'\nPara pintar essa parede você precisará de \033[33m{tinta_necessaria:.2f}\033[m l de tinta.')
