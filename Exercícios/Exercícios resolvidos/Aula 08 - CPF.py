from cpf_generator import CPF

cpf = input('Digite seu CPF (apenas números): ')

if CPF.validate(cpf):
    print(f'\nO CPF {CPF.format(cpf)} é VÁLIDO')
else:
    print(f'\nO CPF {CPF.format(cpf)} NÃO é válido')
