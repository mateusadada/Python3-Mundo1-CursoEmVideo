# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um
# triângulo.

print('Bem vindo ao programa de verificação de triângulo!')

reta1 = float(input('1º reta: '))
reta2 = float(input('2º reta: '))
reta3 = float(input('3º reta: '))

if reta1 + reta2 > reta3 and reta1 + reta3 > reta2 and reta2 + reta3 > reta1:
    print('\nÉ possível formar um triângulo!')
else:
    print('\nNÃO é possível formar um triângulo!')
