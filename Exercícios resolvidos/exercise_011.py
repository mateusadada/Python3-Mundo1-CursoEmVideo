# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a
# quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

print('Bem vindo ao programa de cálculo de tinta para pintar uma parede!')

largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
area = largura * altura
tinta_necessaria = area / 2

print(f'\nSua parede tem a dimensão de {largura} x {altura} e sua área é de {area} m².'
      f'\nPara pintar essa parede você precisará de {tinta_necessaria:.2f} l de tinta.')
