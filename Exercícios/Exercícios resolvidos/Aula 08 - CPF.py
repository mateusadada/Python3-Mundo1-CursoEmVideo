from cpf_generator import CPF

print('Bem vindo ao programa de validação de CPF!')

cpf = input('Digite um CPF (apenas números): ')

if CPF.validate(cpf):
    print(f'\nO CPF {CPF.format(cpf)} é válido')
else:
    print(f'\nO CPF {CPF.format(cpf)} NÃO é válido')
