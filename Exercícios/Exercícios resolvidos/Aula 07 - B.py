numero1 = int(input('Digite um valor: '))
numero2 = int(input('Digite outro valor: '))
soma = numero1 + numero2
subtracao = numero1 - numero2
produto = numero1 * numero2
divisao = numero1 / numero2
divisaoInteira = numero1 // numero2
resto = numero1 % numero2
potencia = numero1 ** numero2
raiz = numero1 ** (1/numero2)

print(f'\nO tipo primitivo do {numero1} é {type(numero1)} e do {numero2} é {type(numero2)}')
print(f'A soma é {soma}')
print(f'A subtração é {subtracao}')
print(f'A multiplicação é {produto}')
print(f'A divisão é {divisao:.3f}')
print(f'A divisão inteira é {divisaoInteira}')
print(f'O resto é {resto}')
print(f'A potência é {potencia}')
print(f'A raiz é {raiz:.3f}')
