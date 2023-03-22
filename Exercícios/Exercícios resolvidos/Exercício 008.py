# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

metros = float(input('Uma distância em metros: '))

km = metros/1000
hm = metros/100
dam = metros/10
dm = metros * 10
cm = metros * 100
mm = metros * 1000

print(f'\nA medida de {metros:.2f} corresponde a'
      f'\n{km:.3f} km'
      f'\n{hm:.2f} hm'
      f'\n{dam:.2f} dam'
      f'\n{dm:.2f} dm'
      f'\n{cm:.2f} cm'
      f'\n{mm:.2f} mm')
