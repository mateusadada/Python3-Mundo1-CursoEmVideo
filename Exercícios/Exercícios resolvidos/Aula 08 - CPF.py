from cpf_generator import CPF

print('Bem vindo! Este programa informa se um CPF é válido.')

cpf = input('Digite um CPF (apenas números): ')

if CPF.validate(cpf):
    print(f'\nO CPF {CPF.format(cpf)} é válido')
else:
    print(f'\nO CPF {CPF.format(cpf)} NÃO é válido')
