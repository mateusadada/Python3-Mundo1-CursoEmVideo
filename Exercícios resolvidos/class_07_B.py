print('Bem vindo ao programa de cálculo de várias operações a partir de dois números!')

numero1 = int(input('Digite um valor: '))
numero2 = int(input('Digite outro valor: '))
soma = numero1 + numero2
subtracao = numero1 - numero2
produto = numero1 * numero2
divisao = numero1 / numero2
divisao_inteira = numero1 // numero2
resto = numero1 % numero2
potencia = numero1 ** numero2
raiz = numero1 ** (1/numero2)

print(f'\nO tipo primitivo do \033[33m{numero1}\033[m é \033[33m{type(numero1)}\033[m e do \033[33m{numero2}\033[m'
      f'é \033[33m{type(numero2)}\033[m')
print(f'A soma é \033[33m{soma}\033[m')
print(f'A subtração é \033[33m{subtracao}\033[m')
print(f'A multiplicação é \033[33m{produto}\033[m')
print(f'A divisão é \033[33m{divisao:.3f}\033[m')
print(f'A divisão inteira é \033[33m{divisao_inteira}\033[m')
print(f'O resto é \033[33m{resto}\033[m')
print(f'A potência é \033[33m{potencia}\033[m')
print(f'A raiz é \033[33m{raiz:.3f}\033[m')
