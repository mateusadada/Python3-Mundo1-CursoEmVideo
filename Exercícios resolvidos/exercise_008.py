# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

print('Bem vindo ao programa de conversão de centímetros e milímetros!')

metros = float(input('Uma distância em metros: '))
km = metros/1000
hm = metros/100
dam = metros/10
dm = metros * 10
cm = metros * 100
mm = metros * 1000

print(f'\nA medida de \033[33m{metros:.2f}\033[m corresponde a'
      f'\n\033[33m{km:.3f}\033[m km'
      f'\n\033[33m{hm:.2f}\033[m hm'
      f'\n\033[33m{dam:.2f}\033[m dam'
      f'\n\033[33m{dm:.0f}\033[m dm'
      f'\n\033[33m{cm:.0f}\033[m cm'
      f'\n\033[33m{mm:.0f}\033[m mm')
